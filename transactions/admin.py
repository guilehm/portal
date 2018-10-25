from django.contrib import admin

from transactions.models import DebitNote, DebitNoteItem, Event, EventStatus, Request, ServiceOrder


class DebitNoteItemInline(admin.TabularInline):
    model = DebitNoteItem
    extra = 0
    raw_id_fields = ('debit_note',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('code', 'machine', 'category', 'subject')
    list_filter = ('machine', 'category', 'date_added', 'date_changed')
    readonly_fields = ('company',)


@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ('event', 'status', 'date_added')
    list_filter = ('status', 'date_added', 'date_changed')


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'event', 'category', 'machine', 'priority')
    list_filter = ('category', 'priority')
    search_fields = ('event', 'category', 'subject', 'description')
    readonly_fields = ('company',)


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('code', 'category', 'machine', 'date')
    list_filter = ('category', 'date')
    search_fields = ('subject', 'machine', 'category')


@admin.register(DebitNote)
class DebitNoteAdmin(admin.ModelAdmin):
    list_display = ('code', 'reference', 'service_order', 'company', 'status', 'total')
    list_filter = (
        'status',
        ('company', admin.RelatedOnlyFieldListFilter)
    )
    search_fields = ('reference', 'comments', 'company')
    readonly_fields = ('company', 'total')
    inlines = (DebitNoteItemInline,)


@admin.register(DebitNoteItem)
class DebitNoteItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'debit_note', 'total')
    list_filter = ('date',)
    search_fields = ('description',)
    readonly_fields = ('total',)
