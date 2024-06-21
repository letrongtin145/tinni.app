from django.urls import path

from . import views

app_name = 'about_us'
urlpatterns = [

    # Trang chủ
    # ex: /about-us
    path('', views.about, name='dashboard'),
]
