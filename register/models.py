from django.db import models


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
