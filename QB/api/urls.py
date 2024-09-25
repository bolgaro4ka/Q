from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('post/', views.StatusView.as_view()),
    path('qvpn/', views.QVPNView.as_view()),
]