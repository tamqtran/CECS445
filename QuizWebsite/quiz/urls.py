from django.urls import path

from . import views
app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('HowToPlay/', views.HowToPlay, name ='HowToPlay'),
    path('AboutUs/', views.About, name ='About'),
]
