from django.contrib import admin

from files.models import DataFile, Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'date_added')
    list_filter = ('date_added', 'date_changed')


@admin.register(DataFile)
class DataFileAdmin(admin.ModelAdmin):
    list_filter = ('extension',)
    list_display = ('id', 'original_file_name', 'extension')
    search_fields = ('original_file_name',)
