from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic import edit, base
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from .forms import ContactUs

from .models import FlexSlide, AboutCardSection, AboutCardTopic, BenefitSection, BenefitTopic, AdvantageTopic\
                    , HowItWorksSection, HowItWorksTopic, PartnersSection, PartnerIcon, CounterSection, TestimonialSection

import requests
import operator
from django.contrib import messages
from django.conf import settings
import urllib
import urllib.request as urllib2
import json

class HomeView(base.TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        flex_slide = None
        about_card_section = None
        about_card_topics = None
        benefit_section = None
        benefit_topics = None
        advantage_topics = None
        howitworks_section = None
        howitworks_topics = None
        partners_section = None
        partners = None
        counter_section = None
        testimonials = None

        try:
            flex_slide = FlexSlide.objects.all().order_by('-created_at')[:3]
        except FlexSlide.DoesNotExist:
            flex_slide = None

        try:
            about_card_section = AboutCardSection.objects.get(active=True)
            about_card_topics = about_card_section.topics_set.all().order_by('created_at')
        except AboutCardSection.DoesNotExist:
            about_card_section = None
            about_card_topics = None

        try:
            benefit_section = BenefitSection.objects.get(active=True)
            benefit_topics = benefit_section.benefit_set.all().order_by('created_at')
        except BenefitSection.DoesNotExist:
            benefit_section = None
            benefit_topics = None

        try:
            howitworks_section = HowItWorksSection.objects.get(active=True)
            howitworks_topics = howitworks_section.howitworks_set.all().order_by('created_at')
        except HowItWorksSection.DoesNotExist:
            howitworks_section = None
            howitworks_topics = None

        try:
            partners_section = PartnersSection.objects.get(active=True)
            partners = partners_section.partners_set.all().order_by('created_at')
        except PartnersSection.DoesNotExist:
            partners_section = None
            partners = None

        advantage_topics = AdvantageTopic.objects.all().order_by('created_at')
        counter_section = CounterSection.objects.all()
        testimonials = TestimonialSection.objects.all().order_by('-created_at')

        context.update({
        'flex_slide': flex_slide
        , 'about_card_section': about_card_section
        , 'about_card_topics': about_card_topics
        , 'benefit_section': benefit_section
        , 'benefit_topics': benefit_topics
        , 'advantage_topics': advantage_topics
        , 'howitworks_section': howitworks_section
        , 'howitworks_topics': howitworks_topics
        , 'partners_section': partners_section
        , 'partners': partners
        , 'counter_section': counter_section
        , 'testimonials': testimonials
        , 'contact_us': ContactUs()

        })
        return context

def contact_us(request):
    if request.POST and request.is_ajax():
        form = ContactUs(request.POST)
        data = {}
        print(form.errors)
        if form.is_valid():
            print('entrou valido')
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('recaptcha')
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=values)
            result = r.json()
            print(result)
            ''' End reCAPTCHA validation '''
            if result['success']:
                print(result)
                form.send_email()
                data['success'] = 'success'
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        else:
            data['error'] = 'error'
            print(data)
        return JsonResponse(data)
    else:
        return HttpResponseRedirect("/")
