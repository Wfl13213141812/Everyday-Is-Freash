from django.shortcuts import render
from .models import *
from goods.models import *
from django.http import JsonResponse
# Create your views here.

#定义购物车
def index(request):

    # carts = Cart.objects.all()
    # 获取用户id
    user_id = request.session.get('user_id')

    # 获取当前用户购物车中所有记录
    carts = Cart.objects.filter(user_id=user_id)

    total = 0
    zongji = 0

    for cart in carts:
        total += cart.amount
        zongji += cart.xiaoji


    return render(request,'cart/cart.html',locals())


# 编写购物车函数
def cart_handle(request):
    # 获取参数
    num = int(request.GET.get('num'))
    good_id = request.GET.get('id')
    good = Goods.objects.get(pk=good_id)

    # print(num,goods_id,good,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    user_id = request.session.get('user_id')


    try:
        cart = Cart.objects.get(user_id=user_id,good_id=good_id)
        cart.amount += num
        cart.xiaoji += num*cart.good.price
        cart.save()

    except:

        cart = Cart()
        cart.good_id = good_id
        cart.amount = num
        cart.xiaoji = num*good.price
        cart.user_id = user_id
        cart.save()
    print('存储成功!!!========================]')
    return JsonResponse({'ret':1})


# 修改购物车
def cart_edit(request):
    # 获取参数
    num = int(request.GET.get('num'))
    id = request.GET.get('id')
    # 获取当前用户
    user_id = request.session.get('user_id')

    # print(num,id,user_id,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

    # 寻找购物车对应商品进行数据修改
    try:
        cart = Cart.objects.get(user_id=user_id,good_id=id)
        cart.amount = num
        cart.xiaoji = num*cart.good.price
        cart.save()
        return JsonResponse({'ret':1})
    except:
        return JsonResponse({'ret':0})


# 删除购物车
def del_cart(request):

    id = request.GET.get('id')

    user_id = request.session.get('user_id')

    try:
        cart = Cart.objects.get(good_id=id,user_id=user_id)
        cart.delete()

        return JsonResponse({'ret':1})
    except:
        return JsonResponse({'ret':0})