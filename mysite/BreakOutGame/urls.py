from django.urls import path

from . import views

app_name = 'BreakOutGame'
urlpatterns = [path('', views.index, name='index'),]