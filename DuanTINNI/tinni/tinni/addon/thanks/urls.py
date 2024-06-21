from django.urls import path

from . import views

app_name = 'thanks'
urlpatterns = [

    # Trang chủ
    # ex: /home
    path('', views.thanks, name='dashboard'),
]
