from django.shortcuts import render,HttpResponse,redirect
import requests

# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')
def user_list(request):
    # 1.优先去项目根目录的templates中寻找（提前先配置) [不配置就是无效]
    # 2.根据app的注册顺序，在每个app目录下的templates目录寻找user_list.html
    return render(request,"user_list.html")
def user_add(request):
    return render(request,"user_add.html")
def tpl(request):
    name = '韩超'
    roles = ['管理员','保安','CEO']

    user_info = {"name":"张三","sllary":10000,"role":"CTO"}

    data_list = [{"name":"张三","sllary":10000,"role":"CTO"},
                 {"name":"张2","sllary":1000,"role":"CTO"},
                 {"name":"张4","sllary":1000,"role":"CTO"}]
    return render(request,'tpl.html',
                  {"n1":name,
                   "n2":roles,
                   "n3":user_info,
                   "n4":data_list})

def news(request):
    # 1.定义一些新闻（字典或列表）或去数据库 网络请求去联通新闻
    #
    url = 'https://www.chinaunicom.cn/api/article/NewsByIndex/2/2021/11/news'
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    res = requests.get(url,headers=header)
    data_list = res.json()
    print(data_list)
    return render(request,'news.html',{"news_list":data_list})


def something(request):
    # request是一个对象，封装了用户发送过来的所有请求相关的数据

    # 1.获取请求方式
    print(request.method)

    #2.在url上传递值 /something/?n1=123&n2=999
    print(request.GET)

    # 3.在请求体中提交数据
    print(request.POST)

    # 4.【响应】HttpResponse("返回内容")，内容字符串内容返回给请求者
    # return HttpResponse("返回内容")

    # 5.【响应】读取html的内容，进行渲染（替换） 生成 字符串 返回给用户浏览器
    # return render(request,'something.html',{"title":"来了"})

    # 6.【响应】让浏览器你去重定向到其他的页面
    return redirect("www.baidu.com")

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:

        # print(request.POST)
        # return HttpResponse("登录成功！")
        user_name = request.POST.get("user")
        password = request.POST.get('pwd')

        if user_name == 'root' and password == '123':
            # return HttpResponse("登录成功")
            return redirect("www.bilibili.com")
        else:

            # return HttpResponse("登录失败")
            return render(request,'login.html',{"error_msg":"用户名或密码错误"})

from app01.models import Department,UserInfo

def orm(request):
    # 测试ORM表中的数据

    # 新建数据
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")

    # UserInfo.objects.create(name="五",password="123",age = 19)
    # UserInfo.objects.create(name="朱",password="666",age = 29)
    # UserInfo.objects.create(name="朱9",password="666")


    # 删除数据
    UserInfo.objects.filter(id=3).delete()
    # 删除表中全部数据
    Department.objects.all().delete()


    # 获取数据
    #  返回的是列表 data_list = [对象，行,行]  QuerySet类型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #
    #     print(obj.id,obj.name,obj.password,obj.age)

    # # 返回一行数据
    # data1 = UserInfo.objects.filter(id=1).first()
    # print(data1.id,data1.name)
    #


    ### 更新数据
    UserInfo.objects.all().update(password=999)
    return HttpResponse("成功")

def info_list(request):

    data_list = UserInfo.objects.all()
    # print(data_list)

    return render(request,"info_list.html",{"data_list":data_list})

def info_add(request):
    if request.method == "GET":
        return render(request,'info_add.html')
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

    # 添加到数据库

    UserInfo.objects.create(name=user,password=pwd,age=age)

    return  redirect("/info/list/")


# 删除数据

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()

    return redirect("/info/list/")