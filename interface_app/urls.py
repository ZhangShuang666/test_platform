from django.urls import path
from interface_app.views import test_api_views, testcase_views

urlpatterns = [
    # 用例
    path('case_manage/', testcase_views.case_manage),
    path('case_add/', testcase_views.case_add),
    path('save_case/', testcase_views.save_case),
    path('search_case_name/', testcase_views.search_case_name),
    path('case_debug/<int:cid>/', testcase_views.case_debug),

    # api
    path('api_debug/', test_api_views.api_debug),
    path('get_project_list', test_api_views.get_project_list),
    path('get_case_info/', test_api_views.get_case_info),
    path('api_assert/', test_api_views.api_assert),
]
