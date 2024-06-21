"""
URL configuration for tinni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [    
    path('', include('tinni.addon.home.urls')),
    path('about-us', include('tinni.addon.about_us.urls')),
    path('shop', include('tinni.addon.shop.urls')),
    path('services', include('tinni.addon.services.urls')),
    path('blog', include('tinni.addon.blog.urls')),
    path('contact', include('tinni.addon.contact.urls')),
    path('cart', include('tinni.addon.cart.urls')),
    path('checkout', include('tinni.addon.checkout.urls')),
    path('thanks', include('tinni.addon.thanks.urls')),
    path('content', include('tinni.addon.content.urls')),
    path('admin/', admin.site.urls),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)