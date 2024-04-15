from django.shortcuts import render

from mailings.models import Client


# Create your views here.
def index(request):
    context = {
        'object_list': Client.objects.all(),
        'title': 'Рассылки'
    }
    return render(request, 'mailings/index.html', context)
