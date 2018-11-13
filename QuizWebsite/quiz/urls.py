from django.urls import path

from . import views
app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('HowToPlay/', views.HowToPlay, name ='HowToPlay'),
    path('AboutUs/', views.About, name ='About'),
	path('AgeSelection/', views.AgeSelection, name = 'AgeSelection'),
	path('ElementaryCategories/', views.ElementaryCategories, name = 'ElementaryCategories'),
	path('MiddleCategories/', views.MiddleCategories, name = 'MiddleCategories'),
	path('HighCategories/', views.HighCategories, name = 'HighCategories'),
	path('AdultCategories/', views.AdultCategories, name = 'AdultCategories'),
	path('QuizGame/', views.QuizGame, name = 'QuizGame'),
    path('QuizGame/<int:Question_QID>/', views.detail, name='detail'),
    #path('<int:Question_QID>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:Question_QID>/guess/', views.guess, name='guess'),
	path('Result/', views.Result, name = 'Result'),
]
