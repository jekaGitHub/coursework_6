from django.contrib import admin

from mailings.models import Client, Message, SettingsMailing


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


@admin.register(SettingsMailing)
class SettingsMailingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "clients", "message", "start_time", "end_time", "period", "status", "is_active",
                    "user",)
    list_filter = ("status", "period", "is_active", "user",)
    search_fields = ("name", "clients",)
