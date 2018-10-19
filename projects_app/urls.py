from django.contrib import admin
from django.urls import path
from projects_app import views

urlpatterns = [
    path('project_manage/', views.project_manage),
    path('project_add/', views.project_add),
    path('project_edit/<int:pid>/', views.project_edit),
    path('project_delete/<int:pid>/', views.project_delete)
]