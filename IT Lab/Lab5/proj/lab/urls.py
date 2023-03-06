from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('q1', views.q1, name='Q1'),
    path('q2', views.q2, name='Q1'),
    path('q3', views.q3, name='Q1'),
    path('q4', views.q4, name='Q1'),

]