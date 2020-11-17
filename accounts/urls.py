from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('create/', views.AccountCreate.as_view()),
    path('<int:pk>/', views.AccountDetail.as_view()),
]
