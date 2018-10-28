from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome
import os, time
from django.contrib.auth.models import User
from projects_app.models import Project, Module
from selenium.webdriver.support.ui import Select


class ProjectTests(StaticLiveServerTestCase):

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
        #初始化数据
        User.objects.create_user("test01", "test01@mail.com", "password01")
        Project.objects.create(name="测试项目数据", description="项目描述")

        # 登陆
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

    def test_project_manage(self):
        """项目管理测试"""
        self.assertIn("测试项目数据", self.driver.page_source)
        self.assertIn("项目描述", self.driver.page_source)

    def test_project_add(self):
        """项目增加测试"""
        self.driver.find_element_by_id("Create").click()
        time.sleep(1)
        name = self.driver.find_element_by_id("id_name")
        name.send_keys('增加测试项目数据')
        time.sleep(1)
        description = self.driver.find_element_by_id("id_description")
        description.send_keys('增加项目描述')
        time.sleep(1)
        self.driver.find_element_by_id("cerate_project").click()
        time.sleep(1)
        self.assertIn("增加测试项目数据", self.driver.page_source)
        self.assertIn("增加项目描述", self.driver.page_source)

    def test_project_edit(self):
        """项目修改测试"""
        self.driver.find_element_by_link_text("编辑").click()
        time.sleep(1)
        name = self.driver.find_element_by_id("id_name")
        name.clear()
        name.send_keys('修改测试项目数据')
        time.sleep(1)
        description = self.driver.find_element_by_id("id_description")
        description.clear()
        description.send_keys('修改项目描述')
        time.sleep(1)
        self.driver.find_element_by_id("edit_project").click()
        time.sleep(1)
        self.assertIn("修改测试项目数据", self.driver.page_source)
        self.assertIn("修改项目描述", self.driver.page_source)

    def test_project_delete(self):
        """项目删除测试"""
        self.driver.find_element_by_link_text("删除").click()
        time.sleep(1)
        self.assertNotIn("测试项目数据", self.driver.page_source)
        self.assertNotIn("项目描述", self.driver.page_source)



class ModuleTests(StaticLiveServerTestCase):

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
        # 初始化数据
        User.objects.create_user("test01", "test01@mail.com", "password01")
        Project.objects.create(name="测试项目数据", description="项目描述")
        project = Project.objects.get(name="测试项目数据")
        Module.objects.create(name="模块测试", description="模块的描述", project=project)

        # 登陆,并切换到模块
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
        self.driver.find_element_by_id("module_manage").click()
        time.sleep(1)

    def test_module_manage(self):
        """模块管理测试"""
        self.assertIn("模块测试", self.driver.page_source)
        self.assertIn("模块的描述", self.driver.page_source)

    def test_module_add(self):
        """模块增加测试"""
        self.driver.find_element_by_id("CreateM").click()
        time.sleep(1)
        Select(self.driver.find_element_by_id("id_project")).select_by_index(1)
        name = self.driver.find_element_by_id("id_name")
        name.send_keys('增加模块数据')
        time.sleep(1)
        description = self.driver.find_element_by_id("id_description")
        description.send_keys('增加模块描述')
        time.sleep(1)
        self.driver.find_element_by_id("modulu_add").click()
        time.sleep(1)
        self.assertIn("增加模块数据", self.driver.page_source)
        self.assertIn("增加模块描述", self.driver.page_source)

    def test_project_edit(self):
        """模块修改测试"""
        self.driver.find_element_by_link_text("编辑").click()
        time.sleep(1)
        name = self.driver.find_element_by_id("id_name")
        name.clear()
        name.send_keys('修改测试模块数据')
        time.sleep(1)
        description = self.driver.find_element_by_id("id_description")
        description.clear()
        description.send_keys('修改模块描述')
        time.sleep(1)
        self.driver.find_element_by_id("edit_module").click()
        time.sleep(1)
        self.assertIn("修改测试模块数据", self.driver.page_source)
        self.assertIn("修改模块描述", self.driver.page_source)

    def test_project_delete(self):
        """模块测试"""
        self.driver.find_element_by_link_text("删除").click()
        time.sleep(1)
        self.assertNotIn("模块测试", self.driver.page_source)
        self.assertNotIn("模块的描述", self.driver.page_source)



