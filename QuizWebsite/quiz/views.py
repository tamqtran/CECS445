from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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
    latest_question_list = Question.objects.order_by('-QID')[:1]
    template = loader.get_template('QuizGame.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'QuizGame.html')

def Result(request):
    return render(request, 'Result.html')
#Create your views here.

def detail(request, Question_QID):
    return HttpResponse("You're looking at question %s." %  Question_QID)

#def results(request, Question_QID):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % Question_QID)

def guess(request, Question_QID):
    question = get_object_or_404(Question, pk=Question_QID)
    try:
        selected_choice = question.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #selected_choice.votes += 1
        #selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('quiz:results', args=(Question.QID,)))
