from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailings.forms import SettingsMailingForm, MessageForm, ClientForm
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


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:clients')


class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': 'Сообщения для рассылок'
    }


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:messages')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:messages')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:messages')


class SettingsMailingListView(ListView):
    model = SettingsMailing
    extra_context = {
        'title': 'Рассылки'
    }


class SettingsMailingCreateView(LoginRequiredMixin, CreateView):
    model = SettingsMailing
    form_class = SettingsMailingForm
    success_url = reverse_lazy('mailings:mailings')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class SettingsMailingDetailView(LoginRequiredMixin, DetailView):
    model = SettingsMailing


class SettingsMailingUpdateView(LoginRequiredMixin, UpdateView):
    model = SettingsMailing
    form_class = SettingsMailingForm
    success_url = reverse_lazy('mailings:mailings')


class SettingsMailingDeleteView(LoginRequiredMixin, DeleteView):
    model = SettingsMailing
    success_url = reverse_lazy('mailings:mailings')
