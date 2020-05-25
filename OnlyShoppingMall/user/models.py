from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserInfo(AbstractUser):
    """
    用户信息表
    """
    nickname = models.CharField(max_length=32, default="", blank=True)
    phone = models.CharField(max_length=16, default="", blank=True)
    location = models.CharField(max_length=255, default="", blank=True)

    class Meta:
        db_table = "only_user"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
