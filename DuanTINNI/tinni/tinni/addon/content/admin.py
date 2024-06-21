from django.contrib import admin
from tinni.addon.content.models import Content, ContentLocal

# Register your models here.
admin.site.register(ContentLocal) 
admin.site.register(Content) 