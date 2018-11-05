from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

class FlexSlide(models.Model):
    first_phrase = models.CharField("Primeira frase (menor)", max_length=50, blank=False)
    second_phrase = models.CharField("Segunda frase (em destaque)", max_length=50, blank=False)
    slide_image = models.ImageField("Imagem do slide", upload_to='slide_item/%Y/%m/%d/', blank=False)
    active = models.BooleanField("Slide ativo?", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.first_phrase+" "+self.second_phrase

    def __str__(self):
        if self.first_phrase:
            return self.first_phrase
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = FlexSlide.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except FlexSlide.DoesNotExist:
                pass

        return super(FlexSlide, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Slides"

class AboutCardSection(models.Model):
    title = models.CharField("Titulo da seção", max_length=50, blank=False)
    title_bold = models.CharField("Parte do titulo destacado (em negrito)", max_length=50, blank=True, help_text="Este será a parta destacada em nergrito no titulo da seção.")
    description = models.CharField("Descrição", max_length=250, blank=False)
    active = models.BooleanField("Seção ativa?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Seção 'Sobre'"
        verbose_name_plural = "Seções 'Sobre'"

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = AboutCardSection.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except AboutCardSection.DoesNotExist:
                pass

        return super(AboutCardSection, self).save(*args, **kwargs)

class AboutCardTopic(models.Model):
    icon = models.CharField("Nome do ícone do tópico",max_length=200, blank=False, help_text="Este valor se refere ao nome do icone. Para ver a lista com os nomes visite o link: http://themes-lab.com/make-frontend/pages/elements/icons.html")
    title = models.CharField("Título do tópico", blank=False, max_length=50)
    description = RichTextField("Descrição do tópico", blank=True)
    section = models.ForeignKey(AboutCardSection, on_delete=models.PROTECT, verbose_name="Seção ao qual está relacionado", related_name="topics_set")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_next(self):
        next = AboutCardTopic.objects.filter(id__gt=self.id)
        if next:
          return next.first()
        return False

    def get_prev(self):
        prev = AboutCardTopic.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
          return prev.first()
        return False

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    class Meta:
        verbose_name = "Tópico para seção 'Sobre'"
        verbose_name_plural = "Tópicos para seção 'Sobre'"
        ordering = ['-created_at']

class BenefitSection(models.Model):
    title = models.CharField("Titulo da seção", max_length=100, blank=False)
    description = models.CharField("Descrição", max_length=250, blank=False)
    image = models.ImageField("Imagem principal", blank=True)
    active = models.BooleanField("Seção ativa?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Seção 'Benefício'"
        verbose_name_plural = "Seções 'Benefício'"

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = BenefitSection.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except BenefitSection.DoesNotExist:
                pass

        return super(BenefitSection, self).save(*args, **kwargs)

class BenefitTopic(models.Model):
    icon = models.CharField("Nome do ícone do tópico",max_length=200, blank=False, help_text="Este valor se refere ao nome do icone. Para ver a lista com os nomes visite o link: http://themes-lab.com/make-frontend/pages/elements/icons.html")
    title = models.CharField("Título do tópico", blank=False, max_length=50)
    description = models.CharField("Descrição", max_length=250, blank=False)
    section = models.ForeignKey(BenefitSection, on_delete=models.PROTECT, verbose_name="Seção ao qual está relacionado", related_name="benefit_set")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_next(self):
        next = BenefitTopic.objects.filter(id__gt=self.id)
        if next:
          return next.first()
        return False

    def get_prev(self):
        prev = BenefitTopic.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
          return prev.first()
        return False

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    class Meta:
        verbose_name = "Tópico para seção 'Benefício'"
        verbose_name_plural = "Tópicos para seção 'Benefício'"
        ordering = ['-created_at']

class AdvantageTopic(models.Model):
    icon = models.CharField("Nome do ícone do tópico",max_length=200, blank=False, help_text="Este valor se refere ao nome do icone. Para ver a lista com os nomes visite o link: http://themes-lab.com/make-frontend/pages/elements/icons.html")
    title = models.CharField("Título do tópico", blank=False, max_length=50)
    description = models.CharField("Descrição", max_length=250, blank=False)
    active = models.BooleanField("Seção ativa?", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = AdvantageTopic.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except AdvantageTopic.DoesNotExist:
                pass

        return super(AdvantageTopic, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Vantagem"
        verbose_name_plural = "Vantagens"

class HowItWorksSection(models.Model):
    title = models.CharField("Titulo da seção", max_length=100, blank=False)
    title_bold = models.CharField("Parte do titulo destacado (em negrito)", max_length=50, blank=True, help_text="Este será a parta destacada em nergrito no titulo da seção.")
    image = models.ImageField("Imagem principal", blank=True)
    active = models.BooleanField("Seção ativa?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Seção 'Como Funciona'"
        verbose_name_plural = "Seções 'Como Funciona'"

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = HowItWorksSection.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except HowItWorksSection.DoesNotExist:
                pass

        return super(HowItWorksSection, self).save(*args, **kwargs)

class HowItWorksTopic(models.Model):
    icon = models.CharField("Nome do ícone do tópico",max_length=200, blank=False, help_text="Este valor se refere ao nome do icone. Para ver a lista com os nomes visite o link: http://themes-lab.com/make-frontend/pages/elements/icons.html")
    title = models.CharField("Título do tópico", blank=False, max_length=50)
    description = models.CharField("Descrição", max_length=250, blank=False)
    section = models.ForeignKey(HowItWorksSection, on_delete=models.PROTECT, verbose_name="Seção ao qual está relacionado", related_name="howitworks_set")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_next(self):
        next = HowItWorksTopic.objects.filter(id__gt=self.id)
        if next:
          return next.first()
        return False

    def get_prev(self):
        prev = HowItWorksTopic.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
          return prev.first()
        return False

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    class Meta:
        verbose_name = "Tópico para seção 'Como Funciona'"
        verbose_name_plural = "Tópicos para seção 'Como Funciona'"
        ordering = ['-created_at']

class PartnersSection(models.Model):
    title = models.CharField("Título", max_length=255, blank=False)
    title_bold = models.CharField("Parte do titulo destacado (em negrito)", max_length=50, blank=True, help_text="Este será a parta destacada em nergrito no titulo da seção.")
    text = RichTextField("Texto da seção", blank=True)
    author = models.CharField("Autor do texto (caso haja)", max_length=100, blank=True)
    active = models.BooleanField("Seção ativa?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Seção 'Parceiros'"
        verbose_name_plural = "Seções 'Parceiros'"

    def __str__(self):
        if self.title:
            return self.title

        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = PartnersSection.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except PartnersSection.DoesNotExist:
                pass

        return super(PartnersSection, self).save(*args, **kwargs)

class PartnerIcon(models.Model):
    partner_name = models.CharField("Nome do parceiro", max_length=255, blank=False)
    image = models.ImageField("Imagem do parceiro", blank=False, upload_to="partners/icons/%y/%m")
    created_at = models.DateTimeField(auto_now_add=True)
    partner_section = models.ForeignKey(PartnersSection, on_delete=models.PROTECT, verbose_name="Seção relacioada", blank=True, related_name="partners_set")

    def __str__(self):
        if self.partner_name:
            return self.partner_name

        return "Partner name ins't available"

    class Meta:
        verbose_name = "Tópico para seção 'Parceiros'"
        verbose_name_plural = "Tópicos para seção 'Parceiros'"
        ordering = ['-created_at']

class CounterSection(models.Model):
    title = models.CharField("Título do tópico", blank=False, max_length=50)
    counter = models.CharField("Numero", blank=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    class Meta:
        verbose_name = "Contador"
        verbose_name_plural = "Contadores"

class TestimonialSection(models.Model):
    name = models.CharField("Nome", max_length=50, blank=False)
    position = models.CharField("Cargo", max_length=50, blank=False)
    testimonial = RichTextField("Testimonial", blank=True)
    image = models.ImageField("Imagem (Avatar)", blank=True)
    active = models.BooleanField("Testemunho Ativo?", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        if self.name:
            return self.name
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = TestimonialSection.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except TestimonialSection.DoesNotExist:
                pass

        return super(TestimonialSection, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
