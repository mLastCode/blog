from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 用户信息
class User(AbstractUser):

    # 电话号码
    mobile = models.CharField(max_length=11, unique=True, blank=True)

    # 头像信息
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)

    # 个人简介
    user_desc = models.TextField(max_length=500, blank=True)

    # 修改认证的字段
    USERNAME_FIELD = 'mobile'

    # 创建超级管理员的需要必须输入的字段
    REQUIRED_FIELDS = ['username', 'email']

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        db_table = 'tb_user'    # 修改表名
        verbose_name = '用户信息'   # admin 后台显示
        verbose_name_plural = verbose_name  # admin 后台显示

    def __str__(self):
        return self.mobile
