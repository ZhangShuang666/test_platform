from django.shortcuts import render
from projects_app.models import Project
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ProjectForms

@login_required
def project_manage(request):
    username = request.session.get('now_user', '')
    All_Project = Project.objects.all()
    return render(request, 'project_manage.html',
                   {
                       "user": username,
                       "projects": All_Project,       # 传project
                       "type": "list",
                   })


@login_required
def project_add(request):
    username = request.session.get('now_user', '')

    if request.method == 'POST':  # 添加参数后，是post请求了。所以执行这
        # create a form instance and populate it with data from the request:
        form = ProjectForms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            Project.objects.create(name=name, description=description)
            return HttpResponseRedirect('/manage/project_manage/', {type: "list"})

    # if a GET (or any other method) we'll create a blank form
    else:  # 才打开页面时，是get请求，所有执行这里
        form = ProjectForms()

    return render(request, 'project_manage.html',
                  {
                      "user": username,
                      "type": "add",
                      'form': form
                  })


@login_required
def project_edit(request, pid):
    username = request.session.get('now_user', '')

    if request.method == 'POST':  # 添加参数后，是post请求了。所以执行这
        # create a form instance and populate it with data from the request:
        form = ProjectForms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            '''n_p = Project.objects.get(id=pid)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            Project.objects.select_for_update().filter(id=pid).update(name=name)
            Project.objects.select_for_update().filter(id=pid).update(description=description)'''
            print("这里")
            return HttpResponseRedirect('/manage/project_manage/', {type: "list"})

    # if a GET (or any other method) we'll create a blank form
    else:  # 才打开页面时，是get请求，所有执行这里
        #ProjectForms.name=Project.objects.filter(id=pid).get('name')
        #ProjectForms.description=Project.objects.filter(id=pid).get('description')
        form = ProjectForms()


    return render(request, 'project_manage.html',
                  {
                      "user": username,
                      "type": "edit",
                      'form': form,
                      "pid": pid
                  })


def project_delete(request, pid):
    username = request.session.get('now_user', '')

    if request.method == 'POST':  # 添加参数后，是post请求了。所以执行这
        # create a form instance and populate it with data from the request:
        form = ProjectForms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Project.objects.filter(id=pid).delete()
            return HttpResponseRedirect('/manage/project_manage/', {type: "list"})

    # if a GET (or any other method) we'll create a blank form
    else:  # 才打开页面时，是get请求，所有执行这里
        Project.objects.filter(id=pid).delete()
        return HttpResponseRedirect('/manage/project_manage/', {type: "list"})