from django.shortcuts import render
from projects_app.models import Project
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from projects_app.forms import ProjectForms


@login_required
def project_manage(request):
    username = request.session.get('now_user', '')
    All_Project = Project.objects.all()
    return render(request, 'project_manage.html',
                  {
                      "user": username,
                      "projects": All_Project,  # 传project
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
            status = form.cleaned_data['status']
            Project.objects.create(name=name, description=description, status=status)
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
    if request.method == 'POST':  # 添加参数后，是post请求了。所以执行这
        # create a form instance and populate it with data from the request:
        form = ProjectForms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            model = Project.objects.get(id=pid)
            model.name = form.cleaned_data['name']
            model.description = form.cleaned_data['description']
            model.status = form.cleaned_data['status']
            model.save()
            return HttpResponseRedirect('/manage/project_manage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        if pid:
            form = ProjectForms(instance=Project.objects.get(id=pid))

    return render(request, 'project_manage.html',
                  {
                      "type": "edit",
                      'form': form,
                  })


def project_delete(request, pid):
    Project.objects.filter(id=pid).delete()
    return HttpResponseRedirect('/manage/project_manage/', {type: "list"})
