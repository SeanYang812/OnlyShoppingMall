from django.urls import path, re_path
from . import views
urlpatterns = [
    # 支付
    path('pay',),
    # 支付成功回调
    path('success',),
]