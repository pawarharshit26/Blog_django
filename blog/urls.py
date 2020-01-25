from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blogHome, name = 'blogHome'),
    path('<str:slug>', views.blogPost, name = 'blogPost'),
    path('<str:slug>/do_comment', views.do_comment, name = 'do_comment'),
]
