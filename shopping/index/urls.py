from django.contrib import admin
from django.urls import path
from django.urls import include
from index import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index_info/', views.index_info),
    path('addproduct/', views.add_product),
    path('shopdetail-<int:nid>/', views.shopdetail),
    path('login/', views.login),
    path('checkcode.html/', views.check_code),
    path('register/', views.register),
    path('login_user/', views.login_user),
    path('loginout/', views.loginout),
    path('index_top/', views.index_top),
    path('cart/', views.cart),
    path('order/', views.order),
    path('spider_nanzhuang/', views.spider),
    path('taobao-<int:nid>/', views.taobao),
    path('taobao_nvzhuang-<int:nid>/', views.taobao_nvzhuang),
    path('order_info/', views.order_info),
    path('seek/', views.seek),
    path('spider_nvzhuang/', views.spider_nvzhuang),
    path('ttt/', views.ttt)

]