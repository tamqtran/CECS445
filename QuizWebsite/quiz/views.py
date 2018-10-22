from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def HowToPlay(request):
    return render(request, 'HowToPlay.html')

def About(request):
    return render(request, 'About.html')
# Create your views here.
