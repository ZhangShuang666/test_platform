from django.urls import path
from .views import Project_views, Module_views

urlpatterns = [

    # 项目管理
    path('project_manage/', Project_views.project_manage),
    path('project_add/', Project_views.project_add),
    path('project_edit/<int:pid>/', Project_views.project_edit),
    path('project_delete/<int:pid>/', Project_views.project_delete),

    # 模块管理
    path('module_manage/', Module_views.module_manage),
    path('module_add/', Module_views.module_add),
    path('module_edit/<int:mid>/', Module_views.module_edit),
    path('module_delete/<int:mid>/', Module_views.module_delete)
]
