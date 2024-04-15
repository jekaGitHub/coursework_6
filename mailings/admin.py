from django.contrib import admin

from mailings.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "fio", "email", "comment", "user",)
    list_filter = ("user",)
    search_fields = ("fio", "email",)
