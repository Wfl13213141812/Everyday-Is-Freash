#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 20:28
# @Author  : 梁学才
# @Site    : 
# @File    : function.py
# @Software: PyCharm

from django.shortcuts import redirect,reverse


# 装饰器1，检验用户是否登陆
def wapper1(func1):
    def inner(request,*args,**kwargs):
        if request.session.get('user_id'):
            return func1(request,*args,**kwargs)
        else:
            return redirect(reverse('user:login'))
    return inner
