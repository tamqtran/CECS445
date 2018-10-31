from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def HowToPlay(request):
    return render(request, 'HowToPlay.html')

def About(request):
    return render(request, 'About.html')
	
def AgeSelection(request):
    return render(request, 'AgeSelection.html')

def ElementaryCategories(request):
    return render(request, 'ElementaryCategories.html')
	
def MiddleCategories(request):
    return render(request, 'MiddleCategories.html')
	
def HighCategories(request):
    return render(request, 'HighCategories.html')
	
def AdultCategories(request):
    return render(request, 'AdultCategories.html')
	
def QuizGame(request):
    return render(request, 'QuizGame.html')
	
def Result(request):
    return render(request, 'Result.html')
# Create your views here.
