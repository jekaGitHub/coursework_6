from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import index, ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, MessageListView

app_name = MailingsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/view/<int:pk>/', ClientDetailView.as_view(), name='view_client'),
    path('clients/edit/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('messages/', MessageListView.as_view(), name='messages'),
]