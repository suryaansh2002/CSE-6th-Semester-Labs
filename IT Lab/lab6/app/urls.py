from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.home_view, name='home'),
    path('success', views.success_view, name='success'),
    path('first', views.first_form, name='first_form'),
    path('second', views.second_form, name='second_form'),
    path('register', views.register_view, name='register'),
    path('success3', views.success3_view, name='success3'),
    path('device4', views.device_view, name='device4'),
    path('bill4', views.bill4_view, name='device4'),
    
]
