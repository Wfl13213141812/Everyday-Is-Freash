from django.shortcuts import render,redirect,reverse,HttpResponse
from .models import *
from django.core.paginator import Paginator


# Create your views here.


#定义首页
def index(request):

    cags = Cag.objects.all()
    username = request.session.get('username')

    for cag in cags:
        # 给当前分类新设2个属性，
        # 获取当前分类最新的四个商品
        # cag.new_goods = cag.goods_set.all().order_by('-id')[:4]
        # cag.hot_goods = cag.goods_set.all().order_by('-sales')[:3]
        cag.new_goods = Goods.objects.filter(cag=cag).order_by('-id')[:4]
        cag.hot_goods = Goods.objects.filter(cag=cag).order_by('-sales')[:3]

    return render(request, 'goods/index.html', locals())

id_list = []

# 定义分类详情
def detail(request):

    #从列表也 获取 商品 的 具体id
    gid = request.GET.get('gid')

    # print(type(gid),'aaaaaAAAAAAAAAAAAA')

    good = Goods.objects.get(pk=gid)

    # print(good.cag.name,'cCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC')

    cag_id = request.GET.get('cid')

    # print(cag_id,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

    goods = Goods.objects.filter(cag_id=cag_id).order_by()[0:2:-1]

    # print(goods,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

    #获取商品 对象 对其 数据库访问进行加1
    good = Goods.objects.get(pk=gid)
    good.visits+=1
    good.save()


    #声明全局变量
    global id_list

    #用户最近浏览的商品

    if gid not in id_list:
        id_list.append(gid)
    else:
        id_list.remove(gid)
        id_list.append(gid)

    if len(id_list)>5:
        id_list.remove(id_list[0])
    # print(id_list,'======================')

    id_str = '#'.join(id_list)

    # print(id_str, '======================')
    response = render(request,'goods/detail.html',locals())

    response.set_cookie('id_str',id_str,max_age=60*60*24)

    #返回response 页面
    return response


# 定义分类列表
def lists(request):
    # 获取当前 类 id
    cag_id = request.GET.get('cid',1)

    #获取便于设置 查询方式 的id
    show_id = request.GET.get('showid', 1)


    # 默认方式查询当前类
    cag = Cag.objects.get(pk=cag_id)
    if show_id =='1':
        # 匹配默认列表内容
        goods = Goods.objects.filter(cag_id=cag_id)
    if show_id == '2':
        goods = Goods.objects.filter(cag_id=cag_id).order_by('-price')
    if show_id =='3':
        goods = Goods.objects.filter(cag_id=cag_id).order_by('-sales')

    # print(goods,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')


    page = Paginator(goods,15)

    page_list = page.page_range

    number = request.GET.get('number',1)

    current_page = page.page(number)

    # 获取最新商品 展示列表页
    new_goods = Goods.objects.filter(cag_id=cag_id).order_by('-id')[:2]


    return render(request, 'goods/list.html', locals())