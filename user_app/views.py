from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth

# Create your views here.

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
                auth.login(request, user)
                return render(request, "project_manage.html")
            else:
                return render(request, "index.html", {"error": "用户名或者密码错误"})

        #if username == "admin" and password == "admin":
           # return render(request, "project_manage.html")
        #else:
            #return render(request, "index.html", {"error": "用户名或者密码错误"})

