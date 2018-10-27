from django.test import TestCase, Client
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("test01", "test01@mail.com", "password01")

    def test_User_Create(self):
        """测试创建用户"""
        User.objects.create_user("test02", "test02@mail.com", "password02")
        user = User.objects.get(username="test02")
        self.assertEqual(user.username, "test02")

    def test_User_Search(self):
        """测试查询用户"""
        user = User.objects.get(username="test01")
        self.assertEqual(user.email, "test01@mail.com")

    def test_User_update(self):
        """测试更新用户"""
        user = User.objects.get(username="test01")
        user.username = "test02"
        user.email = "test02@mail.com"
        user.password = "password02"
        user.save()
        user2 = User.objects.get(username="test02")
        self.assertEqual(user2.email, "test02@mail.com")

    def test_User_delete(self):
        """测试删除用户"""
        User.objects.get(username="test01").delete()
        user = User.objects.all()
        self.assertEqual(len(user), 0)


class IndexTestCase(TestCase):

    def test_Index(self):
        """测试index登陆页"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class LoginActionTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("test01", "test01@mail.com", "password01")
        self.client = Client()

    def test_Login_Null(self):
        """用户名或者密码为空"""
        Null_data = {
            "username": "",
            "password": ""
        }
        response = self.client.post("/login_action/", data=Null_data)
        html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或者密码为空", html)

    def test_Login_Error(self):
        """用户名或者密码错误"""
        Error_data = {
            "username": "iii",
            "password": "ewr"
        }
        response = self.client.post("/login_action/", data=Error_data)
        html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或者密码错误", html)

    def test_Login_Sucess(self):
        """用户名或者密码错误"""
        Sucess_data = {
            "username": "test01",
            "password": "password01"
        }
        response = self.client.post("/login_action/", data=Sucess_data)
        self.assertEqual(response.status_code, 302)


class LogoutTestCase(TestCase):

    def setUp(self):
        User.objects.create_user("test01", "test01@mail.com", "password01")
        self.client = Client()


    def test_Login_Sucess(self):
        """测试退出"""
        Sucess_data = {
            "username": "test01",
            "password": "password01"
        }
        response = self.client.post("/login_action/", data=Sucess_data)
        self.assertEqual(response.status_code, 302)
        logout_response = self.client.post("/logout/")
        self.assertEqual(logout_response.status_code, 302)
