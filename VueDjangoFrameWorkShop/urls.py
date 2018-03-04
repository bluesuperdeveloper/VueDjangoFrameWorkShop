"""VueDjangoFrameWorkShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

import xadmin
from django.contrib import admin
from django.urls import path, re_path, include

from VueDjangoFrameWorkShop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewset
# from goods.views import GoodsListView,
# from goods.views_base import GoodsListView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })
router = DefaultRouter()

# 配置goods的url,这个basename是干啥的
router.register(r'goods', GoodsListViewSet, base_name="goods")

# 配置Category的url
router.register(r'categories', CategoryViewset, base_name="categories")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),

    # 商品列表页
    # path('goods/', GoodsListView.as_view(),name="goods-list"),
    # path('goods/', goods_list,name="goods-list"),

    # router的path路径
    re_path('^', include(router.urls)),
    # 自动化文档,1.11版本中注意此处前往不要加$符号
    path('docs/', include_docs_urls(title='mtianyan超市文档')),
    # 调试登录
    path('api-auth/', include('rest_framework.urls')),

    # drf自带的token授权登录,获取token需要向该地址post数据
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证
    path('login/', obtain_jwt_token )
]
