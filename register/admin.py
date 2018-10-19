from django.contrib import admin

from register.models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'date_added')
    list_filter = ('date_added', 'date_changed')
