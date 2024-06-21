from django.urls import path

from . import views

app_name = 'services'
urlpatterns = [

    # Trang chủ
    # ex: /about-us
    path('', views.services, name='dashboard'),
]
