from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailings.models import Client, Message, SettingsMailing


# Create your views here.
def index(request):
    context = {
        'object_list': Client.objects.all(),
        'title': 'Статистика по рассылкам'
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


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('mailings:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:clients')


class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': 'Сообщения для рассылок'
    }


class MessageCreateView(CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mailings:messages')


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mailings:messages')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:messages')


class SettingsMailingListView(ListView):
    model = SettingsMailing
    extra_context = {
        'title': 'Рассылки'
    }


class SettingsMailingCreateView(CreateView):
    model = SettingsMailing
    fields = '__all__'
    success_url = reverse_lazy('mailings:mailings')


class SettingsMailingDetailView(DetailView):
    model = SettingsMailing
