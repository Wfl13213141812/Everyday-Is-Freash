from django.shortcuts import render
from cart.models import Cart
from user.models import User
from order.models import Order
import time
from order.models import OrderDetail
from django.http import JsonResponse
import random
# 0: 引入事务
from django.db import transaction


# 引入提交页面需要使用的 防盗链
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#提交订单
def index(request):
    # 查询当前用户
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)

    if request.method == 'GET':

        return render(request,'order/place_order.html',locals())
    if request.method =='POST':
        # 运用 getlist 方法 获取 前端购物车信息 的多个 id
        cart_ids = request.POST.getlist('cart_id')
        # 拼成字符串
        ids_str = '#'.join(cart_ids)

        # 利用 id__in 查询购物车一致的信息
        carts = Cart.objects.filter(id__in = cart_ids)

        return render(request,'order/place_order.html',locals())

# 处理订单
# post 传参 需要使用防盗链装饰器
# 要不使用装饰器 要在 js 中获取csrf_token 的值 一并传入后端且不用获取
@csrf_exempt
# 1: 使用事务装饰器
@transaction.atomic
def order_handle(request):
    # 获取多个id getlist
    pay = request.POST.get('pay')
    ids_str = request.POST.get('ids_str')

    ids_list = ids_str.split('#')
    # 查询购物车记录
    carts = Cart.objects.filter(id__in=ids_list)

    user_id = request.session.get('user_id')

    # print(pay,ids_str,'============================')
    # 2: 创建存档点 保存点
    save_point1 = transaction.savepoint()
    # 判断是否生成订单
    try:
        #     生成订单
        order = Order()
        order.num = str(user_id)+ str(int(time.time()))
        order.fee = 10
        order.status = 1
        order.payway = pay
        order.user_id = user_id
        order.save()

        for cart in carts:

            detail = OrderDetail()
            detail.order = order
            detail.good = cart.good
            detail.num = cart.amount
            detail.xiaoji = cart.xiaoji
            detail.save()

            #存到订单以后 把购物车对应的记录删除
            cart.delete()
        # 3: 订单事务执行成功 提交事务
        transaction.savepoint_commit(save_point1)
        return JsonResponse({'ret':1})
    except:
        # 4: 订单执行失败 ,滚回到保存点
        transaction.savepoint_rollback(save_point1)
        return JsonResponse({'ret':0})


