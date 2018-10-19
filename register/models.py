from django.db import models
from django.utils.functional import cached_property


class Machine(models.Model):
    code = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True, unique=True, db_index=True)
    active = models.BooleanField(default=True, db_index=True)
    # TODO: ForeignKey to Customer

    date_sale = models.DateField(blank=True, null=True)
    date_warranty = models.DateField(blank=True, null=True)
    date_setup = models.DateField(blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.code


class Worker(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    doc = models.CharField(max_length=20, null=True, blank=True, db_index=True, unique=True)
    home_phone_number = models.CharField(max_length=20, null=True, blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True, db_index=True)
    # TODO: ForeignKey to User
    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    @cached_property
    def code(self):
        return f'{self.id:8}'

    @cached_property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @cached_property
    def phone_number(self):
        return self.cell_phone_number or self.home_phone_number or ''
