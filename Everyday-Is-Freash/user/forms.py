#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 19:56
# @Author  : 梁学才
# @Site    : 
# @File    : forms.py
# @Software: PyCharm


from django import forms

class RegisterForms(forms.Form):
    user_name = forms.CharField(error_messages={'required':'此项为必填项'})
    pwd = forms.CharField(error_messages={'required':'此项为必填项'})
    cpwd = forms.CharField(error_messages={'required':'此项为必填项'})
    email = forms.CharField(error_messages={'required':'此项为必填项'})

