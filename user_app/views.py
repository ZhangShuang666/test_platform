from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


#  处理登陆请求
def login_action(request):
    if request.method == "POST":
        #username = request.POST.get("username", "")
        #password = request.POST.get("password", "")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或者密码为空"})

        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)  # 记录用户登陆状态
                request.session["now_user"] = username
                return HttpResponseRedirect('/manage/project_manage/')
            else:
                return render(request, "index.html", {"error": "用户名或者密码错误"})
    else:
        return render(request, "index.html")


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
