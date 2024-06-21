from django.urls import path

from . import views

from django.conf import settings
app_name = 'home'
urlpatterns = [

    # Trang chủ
    # ex: /home
    path('', views.home, name='dashboard'),
] 
