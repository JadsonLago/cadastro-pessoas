import imp
from turtle import home
from django.urls import path
from .views import HomeView

urlpatterns = [
    path('',HomeView.as_view(),name='home')
]