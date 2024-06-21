from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [

    # Trang chủ
    # ex: /about-us
    path('', views.cart, name='dashboard'),
]
