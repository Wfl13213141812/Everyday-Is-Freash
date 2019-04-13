from django.db import models

# Create your models here.
from django.db import models
from user.models import BaseModel
from tinymce.models import HTMLField


# 商品分类模型
class Cag(BaseModel):

    name = models.CharField(max_length=20)


# 商品模型
class Goods(BaseModel):

    # 商品名称
    name = models.CharField(max_length=30)
    # 简介
    short = models.CharField(max_length=100)
    # 详情
    detail = HTMLField()
    # 图片
    img = models.ImageField(upload_to='goods/')
    # 价格
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # 是否上架
    status = models.BooleanField(default=True)
    # 单位
    unit = models.CharField(max_length=10)
    # 访问量
    visits = models.IntegerField()
    # 销量
    sales = models.IntegerField()

    # 分类
    cag = models.ForeignKey(Cag, on_delete=models.CASCADE)
