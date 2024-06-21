from django.shortcuts import render

from tinni.addon.content.models import Content
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):

    obj_data = Content.objects.filter(content_local_id=1).first()
    product = Content.objects.filter(content_local_id=1).all()
    # for i in obj_data:
    #     print(i.content_name)
    
    return render(request, 'home/home.html', {
        'local_data': obj_data, 
        'product': product
    })