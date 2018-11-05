from django.conf.urls import url, include
from fccard.core.views import HomeView as home, contact_us


urlpatterns = [
    url(r'^$', home.as_view(), name='home_page'),
    url(r'^ajax/contact_us$', contact_us, name='contact_us'),
]
