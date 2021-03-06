from django.urls import path
from interface_app.views import test_api_views, testcase_views, task_views, task_api_views


urlpatterns = [
    # 用例view
    path('case_manage/', testcase_views.case_manage),
    path('case_add/', testcase_views.case_add),
    path('search_case_name/', testcase_views.search_case_name),
    path('case_debug/<int:cid>/', testcase_views.case_debug),
    path('case_delete/<int:cid>/', testcase_views.case_delete),


    # 用例api
    path('api_debug/', test_api_views.api_debug),
    path('save_case/', test_api_views.save_case),
    path('get_project_list', test_api_views.get_project_list),
    path('get_case_info/', test_api_views.get_case_info),
    path('api_assert/', test_api_views.api_assert),
    path('save_debug_case/', test_api_views.save_debug_case),

    # 任务view
    path('task_manage/', task_views.task_manage),
    path('task_add/', task_views.task_add),

    # 任务api
    path('get_case_list/', task_api_views.get_case_list),
    path('save_task_data/', task_api_views.save_task_data),


]

