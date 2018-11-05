from django.contrib import admin

from . models import FlexSlide, AboutCardSection, AboutCardTopic, BenefitSection, BenefitTopic, AdvantageTopic\
                    , HowItWorksSection, HowItWorksTopic, PartnersSection, PartnerIcon, CounterSection, TestimonialSection

class AboutCardTopicInline(admin.TabularInline):
    model = AboutCardTopic
    max_num = 4

class AboutCardSectionAdmin(admin.ModelAdmin):
    inlines = [AboutCardTopicInline]

class BenefitTopicInline(admin.TabularInline):
    model = BenefitTopic
    max_num = 5

class BenefitSectionAdmin(admin.ModelAdmin):
    inlines = [BenefitTopicInline]

class HowItWorksTopicInline(admin.TabularInline):
    model = HowItWorksTopic
    max_num = 5

class HowItWorksSectionAdmin(admin.ModelAdmin):
    inlines = [HowItWorksTopicInline]

class PartnerIconInline(admin.TabularInline):
    model = PartnerIcon
    max_num = 8

class PartnersSectionAdmin(admin.ModelAdmin):
    inlines = [PartnerIconInline]

admin.site.register(FlexSlide)
admin.site.register(AboutCardTopic)
admin.site.register(AboutCardSection, AboutCardSectionAdmin)
admin.site.register(BenefitTopic)
admin.site.register(BenefitSection, BenefitSectionAdmin)
admin.site.register(AdvantageTopic)
admin.site.register(HowItWorksTopic)
admin.site.register(HowItWorksSection, HowItWorksSectionAdmin)
admin.site.register(PartnerIcon)
admin.site.register(PartnersSection, PartnersSectionAdmin)
admin.site.register(CounterSection)
admin.site.register(TestimonialSection)
