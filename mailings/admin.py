from django.contrib import admin

from mailings.models import Client, Message, SettingsMailing


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "fio", "email", "comment", "owner",)
    list_filter = ("owner",)
    search_fields = ("fio", "email",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "theme", "body", "owner",)
    list_filter = ("owner",)
    search_fields = ("theme", "body",)


@admin.register(SettingsMailing)
class SettingsMailingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "start_time", "end_time", "period", "status", "is_active",
                    "owner",)
    list_filter = ("status", "period", "is_active", "owner",)
    search_fields = ("name", "clients",)
