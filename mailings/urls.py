from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import (index, ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView,
                            ClientDeleteView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView,
                            MessageDeleteView, SettingsMailingListView, SettingsMailingCreateView,
                            SettingsMailingDetailView)

app_name = MailingsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/view/<int:pk>/', ClientDetailView.as_view(), name='view_client'),
    path('clients/edit/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('messages/create/', MessageCreateView.as_view(), name='create_message'),
    path('messages/view/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('messages/edit/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('messages/delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),
    path('mailings/', SettingsMailingListView.as_view(), name='mailings'),
    path('mailings/create/', SettingsMailingCreateView.as_view(), name='create_mailing'),
    path('mailings/view/<int:pk>/', SettingsMailingDetailView.as_view(), name='view_mailing'),
]