### Django 创建表：

创建数据库表：
```python
from django.db import models


class Project(models.Model):
    """
    项目表
    """
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态：", default=True)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    """
    模块表
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name
```

数据类型查看 ```C:\Python37\Lib\site-packages\django\db\models\fields\__init__.py```

数据库命令：
```python
$ python manage.py makemigrations  #会在当前目录下生成一个migrations文件夹，该文件夹的内容就是数据库要执行的内容 
$ python manage.py migrate         #就是执行之前生成的migrations文件，这一步才是操作数据库的一步

```


### 数据库表操作：

* shell命令
 ```python
$ python manage.py shell
 ```

* 创建
```python
$ Project.objects.create(name="", description="")
```

* 查询
```python
$ Project.objects.all()
$ Project.objects.get(pk=1)
$ Project.objects.filter(status=1)
$ Project.objects.filter(name__contains='项目')
```

* 更新
```python
$ g = Project.objects.get(name='xxx测试项目')
$ g.status=0
$ g.save()

Project.objects.select_for_update().filter(name__contains='项目').update(describe='')
```

* 删除
```python
Project.objects.get(name='xxx测试项目').delete()
```
