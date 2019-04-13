from django.db import models

# Create your models here.

#商品 建模
class Cart(models.Model):
    # 所属用户
    user = models.ForeignKey('user.User',on_delete=models.CASCADE)
    # 商品
    good = models.ForeignKey('goods.Goods',on_delete=models.CASCADE)
    # 数量
    amount = models.IntegerField()
    # 价格小计
    xiaoji = models.DecimalField(max_digits=10,decimal_places=2)


