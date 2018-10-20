from django.contrib import admin

from register.models import Address, Category, Company, DataFile, Machine, Message, Picture, Worker


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'registered_number', 'email')


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('code', 'model', 'serial_number', 'active')
    list_filter = ('model', 'active')
    search_fields = ('code', 'description', 'model', 'serial_number')


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('code', 'full_name', 'doc', 'active')
    search_fields = ('code', 'first_name', 'last_name', 'home_phone_number', 'cell_phone_number')
    list_filter = ('active', 'date_added', 'date_changed')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'active')
    search_fields = ('description',)
    list_filter = ('active', 'date_added', 'date_changed')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('code', 'title')
    search_fields = ('title', 'description')
    list_filter = ('date_added', 'date_changed')


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'date_added')
    list_filter = ('date_added', 'date_changed')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'district', 'city', 'state')
    list_filter = ('city', 'state')
    search_fields = ('address', 'district')


@admin.register(DataFile)
class DataFileAdmin(admin.ModelAdmin):
    list_filter = ('extension',)
    list_display = ('id', 'original_file_name', 'extension')
    search_fields = ('original_file_name',)
