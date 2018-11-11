from django.db import models
from projects_app.models import Module

class TestCase(models.Model):
    """
    用例管理
    """
    module = models.ForeignKey(Module, on_delete=models.CASCADE) # on_delete参数表示项目删除后，模块也跟随删除
    name = models.CharField("名称", max_length=100, blank=False, default="")
    url = models.TextField("URL", default="")
    req_method = models.CharField("方法", max_length=10, default="")
    req_type = models.CharField("参数类型", max_length=10, default="")
    req_header = models.TextField("header", default="")
    req_parameter = models.TextField("参数", default="")
    reponses_assert = models.TextField("验证", default="")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name
