from django.db import models
from django.utils import  timezone
from datetime import date
# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name
#django2.0 要使用String   才能在后台管理里面显示字段名字
#如果发现数据没有在后台管理出现，第一步先检查是否又在amdin里面注册，函数为：admin.site.regesiter(classname,calsname_admin)
class Artical(models.Model):
    pub_data = models.DateField(default=timezone.now)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


