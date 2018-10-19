from django.contrib import admin

from register.models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('code', 'full_name', 'doc', 'active')
    search_fields = ('code', 'first_name', 'last_name', 'home_phone_number', 'cell_phone_number')
    list_filter = ('active', 'date_added', 'date_changed')
