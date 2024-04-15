from django.contrib import admin

from mailings.models import Client, Message


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "fio", "email", "comment", "user",)
    list_filter = ("user",)
    search_fields = ("fio", "email",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "theme", "body", "user",)
    list_filter = ("user",)
    search_fields = ("theme", "body",)
