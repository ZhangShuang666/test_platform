from django.urls import path
from interface_app import views

urlpatterns = [
    path('case_manage/', views.case_manage),
    path('case_add/', views.case_add),
    path('api_debug/', views.api_debug),
    path('save_case/', views.save_case),
    path('get_porject_list', views.get_porject_list),
    path('search_case_name/', views.search_case_name),
    path('case_debug/<int:cid>/', views.case_debug),
]
