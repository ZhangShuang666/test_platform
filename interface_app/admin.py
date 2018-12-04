from django.contrib import admin
from interface_app.models import TestCase, TestTask


class TestcaseAdmin(admin.ModelAdmin):
    list_display = ['module', 'name', 'url', 'req_method', 'req_type', 'req_header', 'req_parameter', 'reponses_assert']


class TestTaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'case_list', 'status', 'create_time']


admin.site.register(TestCase, TestcaseAdmin)
admin.site.register(TestTask, TestTaskAdmin)


