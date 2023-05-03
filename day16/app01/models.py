from django.db import models

# Create your models here.

class Department(models.Model):
    """部门表"""
    # verbose_name 起到注释作用，可写可不写，
    title = models.CharField(verbose_name="部门名称",max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """员工表"""

    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    # 数值的长度为10，小数位为2，默认账户为0
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    # create_time = models.DateTimeField(verbose_name="入职时间")
    create_time = models.DateField(verbose_name="入职时间")

    # 无约束写法
    #1.有约束的
    # to : 与哪一张表关联
    # to_field : 与表中的那一列关联

    #2.django自动写
    #  在下面写的是 depart
    # 到数据库生成的数据列为 ： depart_id

    #3.当部门表中某个部门被删除时

    # 3.1.级联删除，即所有相关员工的信息也被删除
    dapart = models.ForeignKey(verbose_name="部门",to="Department",to_field="id",on_delete=models.CASCADE)

    #3.2.置空，即将相关部门的人员的部门信息置为空
    # null=True,blank=True 表示这一列可以为空，
    # dapart = models.ForeignKey(to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)



    # 在django中的约束，当写入性别时只能写入1 、 2
    gender_choices = (
        (1,"男"),
        (2,"女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name='手机号',max_length=11)

    # 若想为空，则在参数中添加 null=True,blank=Truemi
    price = models.IntegerField(verbose_name="价格",default=0)
    level_choices = (
        (1,"1级"),
        (2,"2级"),
        (3,"3级"),
        (4,"4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别",choices=level_choices,default=1)
    status_choices = (
        (1,"已占用"),
        (2,"未使用"),
    )
    status = models.SmallIntegerField(verbose_name="状态",choices=status_choices,default=2)