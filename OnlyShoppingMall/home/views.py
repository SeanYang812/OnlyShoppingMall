from rest_framework.generics import ListAPIView
from django.core.cache import cache
from common import const
from rest_framework.response import Response
from . import models, serializers


class BannerListAPIView(ListAPIView):
    """
    轮播图视图
    """
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by("-order")[:const.BANNER_COUNT]
    serializer_class = serializers.BannerModelSerializer

    def get(self, request, *args, **kwargs):
        banner_list = cache.get("banner_list")
        if not banner_list:
            print("okkk")
            response = self.list(request, *args, **kwargs)
            print(response)
            cache.set("banner_list", response.data)  # 缓存不设过期时间，更新任务交给celery异步任务框架
            return response

        return Response(banner_list)
