from django.contrib import admin

from transactions.models import Event, ServiceOrder


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('machine', 'category', 'subject')
    list_filter = ('machine', 'category', 'date_added', 'date_changed')


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'event', 'category', 'machine', 'priority')
    list_filter = ('category', 'priority')
    search_fields = ('event', 'category', 'subject', 'description')
