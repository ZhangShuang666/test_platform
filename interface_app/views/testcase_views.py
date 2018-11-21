from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from interface_app.models import TestCase
from interface_app.forms import TestCaseForms
from projects_app.models import Module
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def case_manage(request):
    testcases = TestCase.objects.all()
    paginator = Paginator(testcases, 10)

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
        return render(request, "case_manage.html", {
            "type": "list",
            "testcases": contacts,
        })
    else:
        return HttpResponse("404")


@login_required
# 创建接口
def case_add(request):
    if request.method == "GET":
        form = TestCaseForms()
        return render(request, "case_add.html", {
            "form": form,
            "type": "add"
        })
    else:
        return HttpResponse("404")


def search_case_name(request):
    '''
    搜索用例
    :param request:
    :return:
    '''
    if request.method == "GET":
        case_name = request.GET.get('case_name', "")
        cases = TestCase.objects.filter(name__contains=case_name)

        paginator = Paginator(cases, 2)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # 如果页数不是整型, 取第一页.
            contacts = paginator.page(1)
        except EmptyPage:
            # 如果页数超出查询范围，取最后一页
            contacts = paginator.page(paginator.num_pages)

        return render(request, "case_manage.html", {
            "type": "list",
            "testcases": contacts,
            "case_name": case_name,
        })
    else:
        return HttpResponse("404")


def case_debug(request, cid):
    '''
    调试接口
    :param request:
    :param cid: 用例id
    :return:
    '''
    if request.method == "GET":
        form = TestCaseForms()
        return render(request, "case_debug.html", {
            "form": form,
            "type": "debug"
        })
    else:
        return HttpResponse("404")
