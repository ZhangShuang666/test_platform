from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import json
import requests
from interface_app.models import TestCase
from projects_app.models import Project, Module


def save_case(request):
    '''
    保存测试用例
    :param request:
    :return:
    '''
    if request.method == "POST":
        case_name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        module_name = request.POST.get("module", "")
        reponses_assert = request.POST.get("reponses_assert", "")

        if url == "" or method == "" or req_type == "" or module_name == "":
            return HttpResponse("必传参数为空")

        if parameter == "":
            parameter = "{}"

        if header == "":
            header = "{}"

        module_obj = Module.objects.get(name=module_name)

        case = TestCase.objects.create(name=case_name, module=module_obj, url=url,
                                       req_method=method, req_header=header,
                                       req_type=req_type,
                                       req_parameter=parameter,
                                       reponses_assert=reponses_assert)
        if case is not None:
            return HttpResponse("保存成功！")

    else:
        return HttpResponse("404")


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


def get_project_list(request):
    '''
    获取项目模块列表
    :param request:
    :return:
    '''
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
    编辑用例时，获取接口数据
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

            case_info = {
                "ProjectName": project_name,
                "ModuleName": module_name,
                "name": case_obj.name,
                "url": case_obj.url,
                "reqMethod": case_obj.req_method,
                "reqType": case_obj.req_type,
                "reqHeader": case_obj.req_header,
                "reqParameter": case_obj.req_parameter,
                "reponses_assert": case_obj.reponses_assert
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


def save_debug_case(request):
    '''
    修改用例页面，保存用例
    :param request:
    :return:
    '''
    if request.method == "POST":
        case_id = request.POST.get("case_id", "")
        case_name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        module_name = request.POST.get("module", "")
        reponses_assert = request.POST.get("reponses_assert", "")

        if url == "" or method == "" or req_type == "" or module_name == "":
            return HttpResponse("必传参数为空")

        if parameter == "":
            parameter = "{}"

        if header == "":
            header = "{}"

        module_obj = Module.objects.get(name=module_name)

        case = TestCase.objects.filter(id=case_id).update(name=case_name, module=module_obj, url=url,
                                       req_method=method, req_header=header,
                                       req_type=req_type,
                                       req_parameter=parameter,
                                       reponses_assert=reponses_assert)
        if case is not None:
            return HttpResponse("保存成功！")

    else:
        return HttpResponse("404")

