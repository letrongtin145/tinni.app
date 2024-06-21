from django.urls import path

from . import views

app_name = 'content'
urlpatterns = [

    # Trang chủ
    # ex: /about-us
    path('', views.content, name='dashboard'),
]
