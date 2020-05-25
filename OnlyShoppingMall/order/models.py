from django.db import models
from common.model import BaseModel
from user.models import UserInfo
from commodity.models import Commodity

"""
订单：订单号、流水号、价格、用户
订单详情(自定义关系表)：订单、商品
"""


class Order(BaseModel):
    """
    订单模型
    """
    status_choices = (
        (0, '未支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '超时取消'),
    )
    pay_choices = (
        (1, '支付宝'),
        (2, '微信支付'),
    )
    subject = models.CharField(max_length=150, verbose_name="订单标题")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总价", default=0)
    out_trade_no = models.CharField(max_length=64, verbose_name="订单号", unique=True)
    trade_no = models.CharField(max_length=64, null=True, verbose_name="流水号")
    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="订单状态")
    pay_type = models.SmallIntegerField(choices=pay_choices, default=1, verbose_name="支付方式")
    pay_time = models.DateTimeField(null=True, verbose_name="支付时间")
    user = models.ForeignKey(UserInfo, related_name='user_orders', on_delete=models.DO_NOTHING, db_constraint=False,
                             verbose_name="下单用户")

    # 半自动创建第三张表
    # detail = models.ManyToManyField(to='OrderDetail', through='OrderDetail', through_fields=('order', 'course'))

    class Meta:
        db_table = "only_order"
        verbose_name = "订单记录"
        verbose_name_plural = "订单记录"

    def __str__(self):
        return "%s - ￥%s" % (self.subject, self.total_amount)

    @property
    def commodity(self):
        data_list = []
        for item in self.order_commodity.all():
            data_list.append({
                "id": item.id,
                "commodity_name": item.commodity.name,
                "real_price": item.real_price,
            })

        return data_list


class OrderDetail(BaseModel):
    """
    订单详情
    """
    order = models.ForeignKey(Order, related_name='order_commodity', on_delete=models.CASCADE, db_constraint=False,
                              verbose_name="订单")
    commodity = models.ForeignKey(Commodity, related_name='commodity_orders', on_delete=models.CASCADE,
                                  db_constraint=False,
                                  verbose_name="商品")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="商品原价")
    real_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="商品实价")

    class Meta:
        db_table = "only_order_detail"
        verbose_name = "订单详情"
        verbose_name_plural = "订单详情"

    def __str__(self):
        return "%s的订单：%s" % (self.commodity.name, self.order.out_trade_no)
