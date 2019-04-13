from django.db import models


# 抽象模型，只用来继承
class BaseModel(models.Model):

    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        # 设置为抽象类，在数据库中不生成表，只用来继承
        abstract = True


# 用户模型
class User(BaseModel):

    # 用户名
    username = models.CharField(max_length=20)
    # 密码
    pwd = models.CharField(max_length=64)
    # 邮箱
    email = models.EmailField()
    # 邮编
    code = models.CharField(max_length=10)
    # 地址
    addr = models.CharField(max_length=100)
    # 电话
    tel = models.CharField(max_length=11)
