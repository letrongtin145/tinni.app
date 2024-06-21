from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [

    # Trang chủ
    # ex: /home
    path('', views.shop, name='dashboard'),
]
