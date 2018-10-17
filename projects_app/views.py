from django.shortcuts import render
from projects_app.models import Project
from django.contrib.auth.decorators import login_required

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
    return render(request, 'project_manage.html',
                  {
                      "user": username,
                      "type": "add",
                  })
