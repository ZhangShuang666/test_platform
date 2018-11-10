from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
import json
import requests


@login_required
def case_manage(request):
    return render(request, 'case_manage.html',{
        "type": "list"
    })

@login_required
def debug(request):
    if request.method == "GET":
        return render(request, "api_debug.html", {
            "type": "debug"
        })
    else:
        return HttpResponse("404")

@login_required
def api_debug(request):
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
