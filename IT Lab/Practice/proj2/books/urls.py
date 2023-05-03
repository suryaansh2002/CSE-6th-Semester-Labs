from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('bookForm/', views.bookForm),
    path('books/', views.books),
    path('issueForm/', views.issueForm),
    path('issues/', views.issues),

]
