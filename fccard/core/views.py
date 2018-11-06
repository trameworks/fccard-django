from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import edit, base
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from .forms import ContactUs

from .models import FlexSlide, AboutCardSection, AboutCardTopic, BenefitSection, BenefitTopic, AdvantageTopic\
                    , HowItWorksSection, HowItWorksTopic, PartnersSection, PartnerIcon, CounterSection, TestimonialSection


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
            howitworks_topics = howitworks_section.howitworks_set.all()
        except HowItWorksSection.DoesNotExist:
            howitworks_section = None
            howitworks_topics = None

        try:
            partners_section = PartnersSection.objects.get(active=True)
            partners = partners_section.partners_set.all()
        except PartnersSection.DoesNotExist:
            partners_section = None
            partners = None

        advantage_topics = AdvantageTopic.objects.all()
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
            form.send_email()
            data['success'] = 'success'
        else:
            data['error'] = 'error'
        return JsonResponse(data)
    else:
        return HttpResponseRedirect("/")
