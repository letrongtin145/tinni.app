from django.shortcuts import render

# Create your views here.
def thanks(request):
    return render(request, 'thanks/thanks.html')