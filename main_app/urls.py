from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.landing_page, name="landing"),
    path('about-us', views.about_us, name="about_us"),
    path('contact-us', views.contact_us, name="contact_us"),
    path('power-up/service-request/<slug:service_slug>', views.service_request, name='service_request')
]
