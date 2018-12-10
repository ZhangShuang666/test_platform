from interface_app.models import TestCase, TestTask
from projects_app.models import Project, Module
from common.return_JsonResult import response_false, response_success


def get_case_list(request):
    """
    得到用例list
    :param request:
    :return:
    """
    if request.method == "GET":
        case_list = []
        projects = Project.objects.all()
        for project in projects:
            modules = Module.objects.filter(project_id=project.id)
            for module in modules:
                cases = TestCase.objects.filter(module_id=module.id)
                for case in cases:
                    case_info = project.name + "->" + module.name + "->" + case.name
                    case_dict = {
                        "id": case.id,
                        "name": case_info
                    }
                    case_list.append(case_dict)
        return response_success(data=case_list)
    else:
        return response_false("请求方法错误")


def save_task_data(request):
    """
    保存任务
    :param request:
    :return:
    """
    if request.method == "POST":
        name = request.POST.get("task_name", "")
        describe = request.POST.get("task_describe", "")
        cases = request.POST.get("task_cases", "")

        if name == "":
            return response_false("任务的名称不能为空")

        # 保存数据库
        task = TestTask.objects.create(name=name, description=describe, case_list=cases)
        if task is None:
            return response_false("创建失败")

        return response_success(message="创建任务成功！")
    else:
        return response_false("请求方法错误")
