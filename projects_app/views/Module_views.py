from django.shortcuts import render
from projects_app.models import Module
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from projects_app.forms import ModuleForms


@login_required
def module_manage(request):
    All_Modules = Module.objects.all()
    return render(request, 'module_manage.html',
                  {
                      "modules": All_Modules,  # 传project
                      "type": "list",
                  })


@login_required
def module_add(request):

    if request.method == 'POST':  # 添加参数后，是post请求了。所以执行这
        # create a form instance and populate it with data from the request:
        form = ModuleForms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            Module.objects.create(name=name, description=description, project=project)
            return HttpResponseRedirect('/manage/module_manage/', {type: "list"})

    # if a GET (or any other method) we'll create a blank form
    else:  # 才打开页面时，是get请求，所有执行这里
        form = ModuleForms()

    return render(request, 'module_manage.html',
                  {
                      "type": "add",
                      'form': form
                  })


@login_required
def module_edit(request, mid):
    if request.method == 'POST':  # 添加参数后，是post请求了。所以执行这
        # create a form instance and populate it with data from the request:
        form = ModuleForms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            model = Module.objects.get(id=mid)
            model.project = form.cleaned_data['project']
            model.name = form.cleaned_data['name']
            model.description = form.cleaned_data['description']
            model.save()
            return HttpResponseRedirect('/manage/module_manage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        if mid:
            form = ModuleForms(instance=Module.objects.get(id=mid))

    return render(request, 'module_manage.html',
                  {
                      "type": "edit",
                      'form': form,
                  })


def module_delete(request, mid):
    Module.objects.filter(id=mid).delete()
    return HttpResponseRedirect('/manage/module_manage/', {type: "list"})
