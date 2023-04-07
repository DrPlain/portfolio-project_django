from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landing-home'),
    path('about', views.about, name='landing-about'),
    path('subscribe', views.subscribe, name='subscribe')
]