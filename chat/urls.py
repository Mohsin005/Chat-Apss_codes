from django import urls
from django.urls import path
from .import views

urlpatterns = [
    path('chat/',views.index,name='chat'),

]
