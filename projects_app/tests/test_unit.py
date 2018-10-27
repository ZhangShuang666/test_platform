from django.test import TestCase, Client
from django.contrib.auth.models import User
from projects_app.models import Project, Module


class ProjectTestCase(TestCase):

    def setUp(self):
        User.objects.create_user("test01", "test01@mail.com", "password01")
        Project.objects.create(name="测试项目数据", description="项目描述")
        self.clent = Client()
        Sucess_data = {
            "username": "test01",
            "password": "password01"
        }
        self.client.post("/login_action/", data=Sucess_data)

    def test_project_manage(self):
        """项目管理测试"""
        response = self.client.get("/manage/project_manage/")
        project_mange_html = response.content.decode("utf-8")
        self.assertIn("测试项目数据", project_mange_html)
        self.assertIn("项目描述", project_mange_html)

    def test_project_add(self):
        """项目增加测试"""
        add_data = {
            "name":"增加测试项目",
            "description":"增加的项目的描述"
        }
        self.client.post("/manage/project_add/", data=add_data)
        list_response = self.client.get("/manage/project_manage/")
        project_add_html = list_response.content.decode("utf-8")
        self.assertIn("增加测试项目", project_add_html)
        self.assertIn("增加的项目的描述", project_add_html)

    def test_project_edit(self):
        """项目修改测试"""
        project = Project.objects.get(name="测试项目数据")
        edit_data = {
            "name":"项目修改后的名称",
            "description":"项目修改后的描述",
        }
        self.client.post("/manage/project_edit/{0}/".format(project.id), data=edit_data)
        list_response = self.client.get("/manage/project_manage/")
        project_edit_html = list_response.content.decode("utf-8")
        self.assertIn("项目修改后的名称", project_edit_html)
        self.assertIn("项目修改后的描述", project_edit_html)

    def test_project_delete(self):
        """项目删除测试"""
        project = Project.objects.get(name="测试项目数据")
        self.client.post("/manage/project_delete/{0}/".format(project.id))
        list_response = self.client.get("/manage/project_manage/")
        project_delete_html = list_response.content.decode("utf-8")
        self.assertNotIn("测试项目数据", project_delete_html)
        self.assertNotIn("项目描述", project_delete_html)


class ModuleTestCase(TestCase):

    def setUp(self):
        User.objects.create_user("test01", "test01@mail.com", "password01")
        Project.objects.create(name="测试项目数据", description="项目描述")
        project = Project.objects.get(name="测试项目数据")
        Module.objects.create(name="模块测试", description="模块的描述", project=project)
        self.clent = Client()
        Sucess_data = {
            "username": "test01",
            "password": "password01"
        }
        self.client.post("/login_action/", data=Sucess_data)

    def test_module_manage(self):
        """模块管理测试"""
        response = self.client.get("/manage/module_manage/")
        project_mange_html = response.content.decode("utf-8")
        self.assertIn("模块测试", project_mange_html)
        self.assertIn("模块的描述", project_mange_html)

    def test_module_add(self):
        """模块增加测试"""
        project = Project.objects.get(name="测试项目数据")
        add_data = {
            "name":"增加测试模块",
            "description":"增加的模块的描述",
            "project": project.id
        }
        self.client.post("/manage/module_add/", data=add_data)
        list_response = self.client.get("/manage/module_manage/")
        module_add_html = list_response.content.decode("utf-8")
        self.assertIn("增加测试模块", module_add_html)
        self.assertIn("增加的模块的描述", module_add_html)

    def test_module_edit(self):
        """模块修改测试"""
        project = Project.objects.get(name="测试项目数据")
        module = Module.objects.get(name="模块测试")
        edit_data = {
            "name":"模块修改后的名称",
            "description":"模块修改后的描述",
            "project": project.id
        }
        self.client.post("/manage/module_edit/{0}/".format(module.id), data=edit_data)
        list_response = self.client.get("/manage/module_manage/")
        module_edit_html = list_response.content.decode("utf-8")
        self.assertIn("模块修改后的名称", module_edit_html)
        self.assertIn("模块修改后的描述", module_edit_html)

    def test_project_delete(self):
        """模块删除测试"""
        module = Module.objects.get(name="模块测试")
        self.client.post("/manage/module_delete/{0}/".format(module.id))
        list_response = self.client.get("/manage/module_manage/")
        module_delete_html = list_response.content.decode("utf-8")
        self.assertNotIn("模块测试", module_delete_html)
        self.assertNotIn("模块的描述", module_delete_html)
