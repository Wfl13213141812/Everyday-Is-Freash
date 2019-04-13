from django.test import TestCase
from .models import *
import random

# 给分类插入测试数据
cags = ['新鲜水果', '海鲜水产', '猪牛羊肉', '禽类蛋品', '新鲜蔬菜', '速冻食品']

for g in cags:
    cag = Cag()
    cag.name = g
    cag.save()

units = ['500克', '1吨', '2个', '3条', '1包', '5支', '1头', '2瓶', '1套', '1枚']

# 给商品插入测试数据
with open(r'E:\FIreclass\BJ.Dj_flask\Project\TTSX\data.txt', 'r', encoding='utf-8') as f:

    for goodsname in f:
        # 每循环一次，创建一条商品记录
        good = Goods()
        good.name = goodsname[:-1]  # 把goodsname最后面的换行符去掉
        good.short = '商品非常好，一天销量破百万'
        good.detail = '商品非常详细的描述, 可能包括图片，文字大小和颜色'
        good.img = 'goods/' + str(random.randint(1, 18)) + '.jpg'
        good.price = random.randint(5, 1000)
        good.unit = units[random.randint(0, 9)]
        good.cag_id = random.randint(1, 6)
        good.visits = 0
        good.sales = 0
        good.save()
