from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import json
import requests
from interface_app.models import TestCase
from projects_app.models import Project, Module


@login_required
def api_debug(request):
    '''
    接口返回值，返回到页面
    :param request:
    :return:
    '''
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")
        header = request.POST.get("header")

        payload = json.loads(parameter.replace("'", "\""))

        if method == "get":
            r = requests.get(url, params=payload, headers=header)

        if method == "post":
            r = requests.post(url, data=payload, headers=header)

        return HttpResponse(r.text)


# 获取项目模块列表
def get_project_list(request):
    project_list = Project.objects.all()
    dataList = []
    for project in project_list:
        project_dict = {
            "name": project.name
        }
        module_list = Module.objects.filter(project_id=project.id)
        if len(module_list) != 0:
            module_name = []
            for module in module_list:
                module_name.append(module.name)

            project_dict["moduleList"] = module_name
            dataList.append(project_dict)

    return JsonResponse({"success": "true", "data": dataList})


def get_case_info(request):
    '''
    获取接口数据
    :param request:
    :return:
    '''
    if request.method == "POST":
        case_id = request.POST.get("caseId", "")
        if case_id == "":
            return HttpResponse("404")
        else:
            case_obj = TestCase.objects.get(pk=case_id)
            module_obj = Module.objects.get(pk=case_obj.module_id)
            module_name = module_obj.name

            project_obj = Project.objects.get(pk=module_obj.project_id)
            project_name = project_obj.name

            print(project_name, module_name)

            case_info = {
                "ProjectName": project_name,
                "ModuleName": module_name,
                "name": case_obj.name,
                "url": case_obj.url,
                "reqMethod": case_obj.req_method,
                "reqType": case_obj.req_type,
                "reqHeader": case_obj.req_header,
                "reqParameter": case_obj.req_parameter,
            }
            return JsonResponse({
                "success": "true",
                "data": case_info
            })


def api_assert(request):
    """
    对测试用例的断言进行验证
    :param request:
    :return:
    """
    if request.method == "POST":
        result_text = request.POST.get("result_text", "")
        assert_text = request.POST.get("assert_text", "")

        if result_text == "" or assert_text == "":
            return JsonResponse(
                {
                    "success": "false",
                    "message": "null"
                }
            )

        try:
            assert assert_text in result_text
        except AssertionError:
            return JsonResponse({
                "success": "false",
                "message": "验证失败"
            })
        else:
            return JsonResponse(
                {
                    "success": "true",
                    "message": "验证成功"
                }
            )
    else:
        return JsonResponse({
            "success": "false",
            "message": "请求方法错误"
        })
