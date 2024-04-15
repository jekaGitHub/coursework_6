from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import index, ClientListView, ClientCreateView

app_name = MailingsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/create/', ClientCreateView.as_view(), name='create_client'),
]