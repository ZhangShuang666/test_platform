from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from interface_app.models import TestCase, TestTask
from interface_app.forms import TestCaseForms
from projects_app.models import Module
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def task_manage(request):
    '''
    显示任务列表
    :param request:
    :return:
    '''
    tasks = TestTask.objects.all().order_by('create_time')
    paginator = Paginator(tasks, 10)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)

    if request.method == "GET":
        return render(request, "task_manage.html", {
            "type": "list",
            "tasks": contacts,
        })
    else:
        return HttpResponse("404")


def task_add(request):
    '''
    创建任务
    :param request:
    :return:
    '''
    if request.method == "GET":
        return render(request, "task_add.html", {
            "type": "add"
        })
    else:
        return HttpResponse("404")