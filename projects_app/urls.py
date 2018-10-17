from django.contrib import admin
from django.urls import path
from projects_app import views

urlpatterns = [
    path('project_manage/', views.project_manage),
    path('project_add/', views.project_add),
]