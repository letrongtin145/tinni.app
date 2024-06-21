from django.shortcuts import render

from tinni.addon.content.models import Content

# Create your views here.
def services(request):

    obj_data = Content.objects.filter(content_local_id=4).first()
    # for i in obj_data:
    #     print(i.content_name)
    return render(request, 'services/services.html', {
     'local_data': obj_data
    })