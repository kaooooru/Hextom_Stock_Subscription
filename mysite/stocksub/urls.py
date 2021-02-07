from django.urls import path

from . import views

app_name = 'stocksub'
urlpatterns = [
    path('', views.index, name='index'),
    path('thanks', views.thanks, name='thanks'),
]