from django.shortcuts import render

def home(requests):
    return render(requests, 'landing_page/home.html')

def about(requests):
    return render(requests, 'landing_page/about.html')