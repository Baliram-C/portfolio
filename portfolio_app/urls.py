from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('service-details/', views.service_details, name='service-details'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]