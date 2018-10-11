from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from user_app.models import Project


def index(request):
    return render(request, "index.html")

#  处理登陆请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或者密码为空"})

        else:
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)  # 记录用户登陆状态
                request.session["now_user"] = username
                return HttpResponseRedirect('/project_manage/')
                #return render(request, "project_manage.html")
            else:
                return render(request, "index.html", {"error": "用户名或者密码错误"})

@login_required
def project_manage(request):
    username = request.session.get('now_user', '')
    All_Project = Project.objects.all()
    return render(request, 'project_manage.html',
                   {
                       "user": username,
                       "projects": All_Project,       # 传project
                   })


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")