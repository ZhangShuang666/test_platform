from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome
import os, time
from django.contrib.auth.models import User


class LoginTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        path = os.getcwd() + "/driver/chromedriver"
        super().setUpClass()
        cls.driver = Chrome(path)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        User.objects.create_user("test01", "test01@mail.com", "password01")

    def test_login_null(self):
        """用户名密码为空"""
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('')
        time.sleep(1)
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('')
        time.sleep(1)
        self.driver.find_element_by_id("signin").click()
        ErrorNote = self.driver.find_element_by_id("ErrorNote").text
        time.sleep(2)
        self.assertEqual("用户名或者密码为空", ErrorNote)

    def test_login_error(self):
        """用户名密码错误"""
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('test01')
        time.sleep(1)
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('test01')
        time.sleep(1)
        self.driver.find_element_by_id("signin").click()
        ErrorNote = self.driver.find_element_by_id("ErrorNote").text
        time.sleep(2)
        self.assertEqual("用户名或者密码错误", ErrorNote)

    def test_login_sucess(self):
        """登陆成功"""
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('test01')
        time.sleep(1)
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('password01')
        time.sleep(1)
        self.driver.find_element_by_id("signin").click()
        navbar_brand = self.driver.find_element_by_class_name("navbar-brand").text
        time.sleep(1)
        self.assertEqual("测试平台", navbar_brand)


class LogoutTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        path = os.getcwd() + "/driver/chromedriver"
        super().setUpClass()
        cls.driver = Chrome(path)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        User.objects.create_user("test01", "test01@mail.com", "password01")

    def test_logout(self):
        """测试退出登陆"""
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('test01')
        time.sleep(1)
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('password01')
        time.sleep(1)
        self.driver.find_element_by_id("signin").click()
        time.sleep(1)
        self.driver.find_element_by_id("SignOut").click()
        time.sleep(1)
        button = self.driver.find_element_by_id("signin").text
        self.assertEqual("Sign in", button)
