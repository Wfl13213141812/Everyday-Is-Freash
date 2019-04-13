from django.shortcuts import render,redirect,reverse,HttpResponse
from django.views.generic.base import View
from .forms import *
from .models import *
from .function import *
from goods.models import *
from order.models import Order
from django.core.paginator import Paginator


# Create your views here.

#用户注册
class Register(View):
    def get(self,request):

        return render(request,'user/register.html',locals())
    def post(self,request):

        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        #判断用户是否存在

        users = User.objects.filter(username=username)
        emails = User.objects.filter(email=email)

        flag = True

        if len(users)>0:
            name_error ='用户名已注册'
            flag = False

        if len(emails)>0:
            email_error = '邮箱已注册'
            flag = False

        if pwd != cpwd:
            pwd_error = '两次密码输入不一致'
            flag = False
        if not allow:
            allow_error = '未勾选同意协议'
            flag = False
        # 根据flag 最终的值判断是否存入数据库
        print(flag,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

        if flag:
            us = User()
            us.username = username
            us.pwd = pwd
            us.email = email
            us.save()

            return render(request,'user/login.html',locals())
        else:
            return render(request,'user/register.html',locals())




#用户登录
def login(request):
    if request.method =='GET':

        return render(request,'user/login.html',locals())
    if request.method=='POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        remb = request.POST.get('remember')
        # print(username,pwd,remb,'BBBBAAAAAAAAAAAAAAAAAAAAAAAAAA')

#         判断用户是否存在
    users = User.objects.filter(username=username)
    if len(users)==0:
        name_error='用户名不存在,请刷新重试！！！'
        return render(request,'user/login.html',locals())
    else:
#           状态保持
        request.session['user_id']=users[0].id
        request.session['username']=username

        # 从cookie中 获取最近依次浏览的url
        # 若果没有最近的url 将跳转到默认页面

        pre_url = request.COOKIES.get('pre_url',reverse('goods:index'))

        response = redirect(pre_url)

#         判断是否需要记住用户名
        if remb:
            # 把用户名设置为cookie
            response.set_cookie('username',username.encode('utf-8').decode('latin-1'),max_age=60*60*24)
        else:
            response.delete_cookie('username')
        return redirect(reverse('goods:index'))


# 退出登陆
def logout(request):
    # 获取最近浏览的url
    pre_url = request.COOKIES.get('pre_url')
    # print(pre_url,'BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    # 退出登陆，清空session
    request.session.flush()
    return redirect(pre_url)




#个人信息
@wapper1
def info(request):

    username = request.session.get('username')
    uid = request.session.get('user_id')
    # print(username,uid,'BBBBBBBBBBBBBBBBBBBBBBBBBB')
    user = User.objects.get(pk=uid)


    #获取用户浏览商品id
    id_str = request.COOKIES.get('id_str','')

    if id_str!='':
        id_str = id_str.split('#')
        records = []
        for id in id_str:
            good = Goods.objects.get(pk=id)
            records.append(good)

        records[::-1]

    return render(request,'user/user_center_info.html',locals())



#全部订单
@wapper1
def order(request):

    # 查询当前用户的所有订单
    orders = Order.objects.all()
    # 每个订单的总价
    for order in orders:
        zongjia = 0
        for detail in order.orderdetail_set.all():
            # 给每个订单新增总价属性
            zongjia+=detail.xiaoji

        order.zongjia = zongjia


    # 分页
    pages = Paginator(orders,2)
    num_list = pages.page_range

    page_id = request.GET.get('page_id',1)

    current_page = pages.page(page_id)

    return render(request,'user/user_center_order.html',locals())



#收货地址
@wapper1
def site(request):

    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)

    if request.method == 'GET':

        return render(request,'user/user_center_site.html',locals())
    else:
        username = request.POST.get('username')
        addr = request.POST.get('addr')
        code = request.POST.get('code')
        tel = request.POST.get('tel')

        # print(username,addr,code,tel,'Baaaaaaaaaaaaaaa')

        if username!='' and addr !='' and len(tel)==11:
            user.username = username
            user.addr = addr
            user.code = code
            user.tel = tel

            user.save()

            pre_url = request.COOKIES.get('pre_url')

            return redirect(reverse('user:site'))




