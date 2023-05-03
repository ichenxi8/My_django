from django.shortcuts import render,redirect
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from django.utils.safestring import mark_safe
from app01.utils.pagination import Pagination

def depart_list(request):
    """部门 列表"""
    # 获取数据库中所有的部门列表
    queryset = models.Department.objects.all()

    return render(request,'depart_list.html',{'queryset':queryset})

def depart_add(request):
    """添加部门"""

    if request.method == "GET":
        return render(request,'depart_add.html')
    # 获取用户通过post提交的数据
    title = request.POST.get("title")
    print(title)
    # 保存到数据库

    models.Department.objects.create(title=title)

    # 重定向回部门列表
    return  redirect("/depart/list/")

def depart_delete(request):

    # 获取ID
    nid = request.GET.get('nid')
    #  删除
    models.Department.objects.filter(id=nid).delete()

    # 跳转回部门列表
    return  redirect("/depart/list/")

def depart_edit(request,nid):
    if request.method == "GET":
        # 根据nid 获取数据
        row_object = models.Department.objects.filter(id=nid).first()
        # print(row_object.id,row_object.title)
        return render(request,'depart_edit.html',{"row_object":row_object})
    # 获取用户提交的标题
    title = request.POST.get("title")
    # 根据ID找到数据库中的数据并进行更新
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")


def user_list(request):
    # 获取数据库中所有的用户列表
    queryset = models.UserInfo.objects.all()
    return render(request,'user_list.html',{"queryset":queryset})

def user_add(request):

    return  render(request,'user_add.html')


#########################
# 基于ModelForm


class UserModelForm(forms.ModelForm):

    # 验证输入的数据
    name = forms.CharField(min_length=3,label="用户名")
    # password  = forms.CharField(label='密码')

    class Meta:
        model = models.UserInfo
        fields = ["name","password","age","create_time","gender","dapart"]
        # widgets = {
            # "name":forms.TextInput(attrs={"class":"form-control"}),
            # "create_time":forms.DateTimeField(attrs={"type":"Date"}),
        # }

    def __init__(self,*args,**kwargs):
        super() .__init__(*args,**kwargs)
        # 循环找到所有的插件，添加class="from-control"
        for name,field in self.fields.items():
            field.widget.attrs = {"class":"form-control","placeholder":field.label}


def user_model_form_add(request):

    # 添加用户
    if request.method == "GET":
        form = UserModelForm()
        return  render(request,"user_model_form_add.html",{"form":form})

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)

        form.save()
        return redirect('/user/list/')
    else:
        # 校验失败
        # print(form.errors)
        return render(request, "user_model_form_add.html", {"form": form})


#编辑用户
def user_edit(request,nid):
    ## 根据ID去数据库获取要编辑的那一行数据
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        ## 显示出默认值

        form = UserModelForm(instance=row_object)
        return render(request,'user_edit.html',{"form":form})

    # POST请求

    # row_object = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    return render(request,'user_edit.html',{"form":form})


# 删除数据
def user_delete(request,nid):

    models.UserInfo.objects.filter(id=nid).delete()
    return  redirect('/user/list/')


# 靓号列表
import random as r
def pretty_list(request):

    # for i in range(300):
    #     m = r.randint(12000000000,19999999999)
    #     p = r.randint(0,500)
    #     l = r.randint(1,4)
    #     s = r.randint(1,2)
    #     models.PrettyNum.objects.create(mobile=m,price=p,level=l,status=s)
    # # 实现搜索功能
    data_list = {}
    search_data = request.GET.get('q')
    if search_data:
        data_list['mobile__contains'] = search_data
    # select * from 表 order_by in level desc;
    # ordeer_by排序，下面语句按照级别排序，符号表示倒序
    # queryset = models.PrettyNum.objects.all().order_by("-level")

    #  分页
    queryset = models.PrettyNum.objects.filter(**data_list).order_by("-level")
    page_object = Pagination(request, queryset, page_size=10)

    page_queryset = page_object.page_queryset
    page_string = page_object.html()

    context = {
        "search_data": search_data,

        "queryset": page_queryset,
        "page_string": page_string
    }
    return render(request,'pretty_list.html',context)

    # total_count = models.PrettyNum.objects.filter(**data_list).order_by("-level").count()


    # # 页码
    # """   <li><a href="/pretty/list/?page=1">1</a></li>
    # """
    # # 总页码
    #
    # total_page_count, div = divmod(total_count,page_size)
    # if div:
    #     total_page_count += 1
    # # 计算出，显示当前页的前5页，后5页
    # plus = 5
    # if total_page_count <= 2 * plus + 1:
    #     start_page = 1
    #     end_page = total_page_count
    # else:
    #     if page <= plus:
    #         start_page = 1
    #         end_page = 2 * plus + 1
    #     else:
    #         start_page = page - plus
    #         end_page = page + plus
    # page_str_list = []
    # for i in range(start_page, end_page + 1):
    #     if i == page:
    #         ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
    #     else:
    #         ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
    #     page_str_list.append(ele)
    #
    # page_string = mark_safe("".join(page_str_list))
    #
    # return render(request, 'pretty_list.html', {"queryset": queryset, "search_data": search_data, "page_string": page_string})
    #


# 添加靓号
class PrettyModelForm(forms.ModelForm):
    #定义校验1，与报错信息
    mobile = forms.CharField(
        label='手机号',
        validators = [RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')]
    )
    class Meta:
        model = models.PrettyNum
        # 展示需要的字段
        fields = ["mobile","price","level","status"]
        # 取出所有的字段
        # fields = "__all__"
        #排除某一个字段
        # exclude = ['level']
    def __init__(self,*args,**kwargs):
        super() .__init__(*args,**kwargs)
        # 循环找到所有的插件，添加class="from-control"
        for name,field in self.fields.items():
            field.widget.attrs = {"class":"form-control","placeholder":field.label}
    # 校验 方式2

    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已经存在")
        # 验证通过，用户输入的值返回
        return txt_mobile
def pretty_add(request):

    if request.method == "GET":
        form = PrettyModelForm()

        return render(request,'pretty_add.html',{"form":form})
    # POST请求

    # row_object = models.UserInfo.objects.filter(id=nid).first()
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    return render(request,'pretty_add.html',{"form":form})

# 编辑靓号
class PrettyEditModelForm(forms.ModelForm):

    # 展示手机号但是限制用户修改
    # mobile = forms.CharField(disabled=True,label="手机号")
    class Meta:
        model = models.PrettyNum
        # 展示需要的字段
        fields = ["mobile","price","level","status"]

    def __init__(self,*args,**kwargs):
        super() .__init__(*args,**kwargs)
        # 循环找到所有的插件，添加class="from-control"
        for name,field in self.fields.items():
            field.widget.attrs = {"class":"form-control","placeholder":field.label}

# 校验 方式2

    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已经存在")
        # 验证通过，用户输入的值返回
        return txt_mobile
def pretty_edit(request, nid):

    row_object = models.PrettyNum.objects.filter(id=nid).first()

    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_object)
        return render(request,'pretty_edit.html',{"form":form})

    form = PrettyEditModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return  redirect('/pretty/list/')
    return render(request,'pretty_edit.html',{'form':form})

def pretty_delete(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')