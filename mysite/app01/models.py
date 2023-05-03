from django.db import models

# Create your models here.
# 写好类后在终端执行以下命令
# python manage.py makemigrations
# python manage.py migrate


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)

#     在表中新增列时，由于已存在列中可能已有数据，所以新增列必须要指定新增列对应的数据
#     1.可以手动输入一个值
#     size = models.CharField(max_length=16)
# #     2.设置一个默认值
#     age = models.IntegerField(default=2)
# #     3.允许为空
#     data = models.IntegerField(null=True,blank=True)

class Department(models.Model):
    title = models.CharField(max_length=16)


