from django.urls import path

from . import views

app_name = 'checkout'
urlpatterns = [

    # Trang chủ
    # ex: /about-us
    path('', views.checkout, name='dashboard'),
]
