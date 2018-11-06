from django import forms
from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import get_template
from django.conf import settings

class ContactUs(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"controled", "placeholder":"NOME", "required":"required", "data-msg-required":"Por favor digite o seu nome"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"controled", "placeholder":"EMAIL", "data-msg-required":"Por favor digite o seu endereço de email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"controled", "placeholder":"MENSAGEM", "data-msg-required":"Por favor digite uma mensagem", "rows":"4"}))

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        subject = "Novo contato - Cavalcante Card"
        html_template = get_template("core/partials/email.html")
        html_message = html_template.render({
            'name': name,
            'email': email,
            'message': message
        })
        try:
            email = EmailMessage(subject, html_message, email, ["cavalcantecard@farmaciacavalcante.com.br"])
            email.content_subtype = "html"
            email.send()
        except BadHeaderError:
            raise ValidationError
