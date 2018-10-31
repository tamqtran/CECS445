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
	path('Result/', views.Result, name = 'Result'),
]
