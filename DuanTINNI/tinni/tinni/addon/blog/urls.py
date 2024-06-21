from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [

    # Trang chủ
    # ex: /blog
    path('', views.blog, name='dashboard'),
]
