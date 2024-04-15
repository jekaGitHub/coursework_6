from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from mailings.models import Client


# Create your views here.
def index(request):
    context = {
        'object_list': Client.objects.all(),
        'title': 'Рассылки'
    }
    return render(request, 'mailings/index.html', context)


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Наши клиенты'
    }


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('mailings:clients')
