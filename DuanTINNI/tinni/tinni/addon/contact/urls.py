from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [

    # Trang chủ
    # ex: /contact
    path('', views.contact, name='dashboard'),
]
