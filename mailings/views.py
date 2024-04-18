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


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Наши клиенты'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


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


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'title': 'Сообщения для рассылок'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


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


class SettingsMailingListView(LoginRequiredMixin, ListView):
    model = SettingsMailing
    extra_context = {
        'title': 'Рассылки'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.groups.filter(name="manager") or user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


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
