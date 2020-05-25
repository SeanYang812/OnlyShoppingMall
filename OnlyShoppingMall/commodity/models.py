from django.db import models
from common.model import BaseModel


class Commodity(BaseModel):
    """
    商品模型
    """
    name = models.CharField(max_length=32, verbose_name="商品名称")
    commodity_img = models.ImageField(upload_to="commodity", max_length=255, verbose_name="封面图片", blank=True, null=True)
    brief = models.TextField(max_length=2048, verbose_name="商品简介", null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='商品价格', default=0)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    orders = models.IntegerField(default=0)

    class Meta:
        db_table = "only_commodity"
        verbose_name = "商品"
        verbose_name_plural = "商品"

    def __str__(self):
        return "%s" % self.name
