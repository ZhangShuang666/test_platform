from django.test import TestCase, Client
from django.contrib.auth.models import User

from projects_app.models import Project, Module
from interface_app.models import TestCase as InterfaceCase


class InterfaceTest(TestCase):
    def setUp(self):
        """
        初始化
        :return:
        """
        User.objects.create_user("test01", "test@mail.com", "test01")
        Project.objects.create(name="新增项目", description="项目描述")
        project = Project.objects.get(name="新增项目")
        Module.objects.create(name="新增模块", description="模块描述",project=project)
        module = Module.objects.get(name="新增模块")
        case = InterfaceCase.objects.create(module=module,name="新增用例1", url="baidu.com",req_method="GET", req_type="JSON", reponses_assert="assert")
        self.client = Client()
        login_data = {
            "username": "test01",
            "password": "test01"
        }
        self.client.post("/login_action/", data=login_data)

    def test_CaseManage(self):
        """
        用例列表测试
        :return:
        """
        response = self.client.get("/interface/case_manage/")
        case_manage_html = response.content.decode("utf-8")
        self.assertIn("新增用例1", case_manage_html)

    def test_SearchCase(self):
        """
        用例搜索测试
        :return:
        """
        search = "新增用例1"
        search2 = "新增用例2"
        response = self.client.get("/interface/search_case_name/", header={"新增用例1"})
        case_search_html = response.content.decode("utf-8")
        self.assertIn("新增用例1", case_search_html)
        self.assertNotIn("新增用例2", case_search_html)

    def test_DeleteCase(self):
        """
        用例删除测试
        :return:
        """
        case = InterfaceCase.objects.get(name="新增用例1")
        print(case)
        print(case.id)
        response= self.client.post("/interface/case_delete/{0}".format(case.id))
        case_manage_html = response.content.decode("utf-8")
        self.assertNotIn("新增用例1", case_manage_html)
