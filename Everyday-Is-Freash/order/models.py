from django.db import models

# Create your models here.
# 订单状态

# 订单模型
class Order(models.Model):
    # 订单号
    num = models.CharField(max_length=50)
    # 创建时间
    c_time = models.DateTimeField(auto_now_add=True)
    # 运费
    fee = models.IntegerField()
    # 订单状态 1-'待付款',2-'待发货',3-'待收货',4-'待评价',
    status = models.CharField(max_length=1)
    #支付方式 1-'货到付款' 2 -'微信支付' 3-'支付宝支付' 4-'银联支付'
    payway = models.CharField(max_length=1)
    # 关联到用户
    user = models.ForeignKey('user.user',on_delete=models.CASCADE)



# 订单详情
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    good = models.ForeignKey('goods.Goods',on_delete=models.CASCADE)
    num = models.IntegerField()
    xiaoji = models.DecimalField(max_digits=10,decimal_places=2)