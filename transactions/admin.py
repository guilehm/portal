from django.contrib import admin

from transactions.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('machine', 'category', 'subject')
    list_filter = ('machine', 'category', 'date_added', 'date_changed')
