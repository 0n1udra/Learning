from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='personal-contact'),
    path('about/', views.about, name='personal-about')
]


