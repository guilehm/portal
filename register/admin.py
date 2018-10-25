from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from register.models import Address, Category, Company, Machine, Message, User, Worker


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
    list_display = ('code', 'full_name', 'active')
    search_fields = ('code', 'first_name', 'last_name')
    list_filter = ('active', 'date_added', 'date_changed')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'active')
    search_fields = ('description',)
    list_filter = ('active', 'date_added', 'date_changed')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('code', 'message')
    search_fields = ('description',)
    list_filter = ('date_added', 'date_changed')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'district', 'city', 'state')
    list_filter = ('city', 'state')
    search_fields = ('address', 'district')


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'woeid')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
        )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'company')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'company')
    ordering = ('username',)
