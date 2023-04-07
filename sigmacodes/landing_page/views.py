from django.shortcuts import render, redirect
from django.contrib import messages


def home(requests):
    return render(requests, 'landing_page/home.html')


def about(requests):
    return render(requests, 'landing_page/about.html')


def subscribe(request):
    if request.method == "POST":
        messages.success(request, 'Successfully subscribed to our newsletters')
        return redirect('landing-home')
