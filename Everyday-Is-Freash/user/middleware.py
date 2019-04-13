#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 19:12
# @Author  : 梁学才
# @Site    : 
# @File    : middleware.py
# @Software: PyCharm

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import reverse


# 记录用户最近一次访问的页面
class PerurlMiddle(MiddlewareMixin):

    # 每次响应后调用
    def process_response(self, request, response):
        # 有些页面的url不需要记录
        not_urls = [
            reverse('user:login'),
            reverse('user:register'),
            reverse('user:info'),
            reverse('user:order'),
            reverse('user:site'),
            reverse('cart:index'),
            reverse('goods:lists'),
            # reverse('user:check_username'),
        ]

        # url不在列表内，并且响应状态码是200，才记录这一次的url
        if request.path not in not_urls and response.status_code == 200:
            response.set_cookie('pre_url', request.path, max_age=60*60*24)
        return response


