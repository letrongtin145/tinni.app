from django.shortcuts import render

from tinni.addon.content.models import Content
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def shop(request):
    try:
        product = Content.objects.filter(content_local_id=2).all()
        obj_data = Content.objects.filter(content_local_id=2).first()
    except:
        product = None
        obj_data = None

    # for i in obj_data:
    #     print(i.content_name)
    return render(request, 'shop/shop.html', {
        'local_data': obj_data,
        'product': product

    })