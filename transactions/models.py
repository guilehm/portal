from decimal import Decimal

from django.conf import settings
from django.db import models
from django.db.models import DecimalField, F, Sum
from django.utils.functional import cached_property


class Event(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='events',
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        'register.Company',
        related_name='events',
        null=True,
        editable=False,
        on_delete=models.CASCADE
    )
    machine = models.ForeignKey(
        'register.Machine',
        related_name='events',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'register.Category',
        related_name='events',
        on_delete=models.CASCADE,
    )
    subject = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    pictures = models.ManyToManyField(
        'files.Picture',
        related_name='events',
        blank=True,
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Event #{id} ({subject})'.format(
            id=self.id,
            subject=self.subject
        )

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(6)

    def save(self, *args, **kwargs):
        if not self.id:
            self.company = self.customer.company
        super().save(*args, **kwargs)


class EventStatus(models.Model):
    NEW = 'new'
    PENDING_CUSTOMER = 'pending_customer'
    PENDING_COMPANY = 'pending_company'
    CLOSED = 'closed'
    SERVICE_ORDER = 'service_order'

    STATUS_CHOICES = (
        (NEW, 'New'),
        (PENDING_CUSTOMER, 'Pending Customer'),
        (PENDING_COMPANY, 'Pending Company'),
        (CLOSED, 'Closed'),
        (SERVICE_ORDER, 'Service Order')
    )
    event = models.ForeignKey(
        'transactions.Event',
        related_name='status',
        db_index=True,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        db_index=True,
        editable=False
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'EventStatus #{id} ({status})'.format(
            id=self.id,
            status=self.status
        )


class ServiceOrder(models.Model):
    LOW = 'low'
    NORMAL = 'normal'
    HIGH = 'high'

    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High')
    )

    event = models.ForeignKey(
        'transactions.Event',
        related_name='service_orders',
        on_delete=models.CASCADE,
    )
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='service_orders',
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        'register.Company',
        related_name='service_orders',
        null=True,
        editable=False,
        on_delete=models.CASCADE
    )
    machine = models.ForeignKey(
        'register.Machine',
        related_name='service_orders',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'register.Category',
        related_name='service_orders',
        on_delete=models.CASCADE
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        db_index=True
    )
    subject = models.CharField(max_length=100)
    description = models.TextField()
    pictures = models.ManyToManyField(
        'files.Picture',
        related_name='service_orders',
        blank=True,
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Service Order #{id} ({subject})'.format(
            id=self.id,
            subject=self.subject
        )

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(6)

    def save(self, *args, **kwargs):
        if not self.id:
            self.company = self.customer.company
        super().save(*args, **kwargs)


class Request(models.Model):
    category = models.ForeignKey(
        'register.Category',
        related_name='requests',
        on_delete=models.CASCADE
    )
    machine = models.ForeignKey(
        'register.Machine',
        related_name='requests',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    subject = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(
        'files.DataFile',
        related_name='requests',
        blank=True
    )
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='requests',
        on_delete=models.CASCADE
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Request #{id} ({subject})'.format(
            id=self.id,
            subject=self.subject
        )

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(6)


class DebitNote(models.Model):
    OPEN = 'open'
    CLOSED = 'closed'

    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
    )

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='debit_notes',
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        'register.Company',
        related_name='debit_notes',
        editable=False,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        db_index=True
    )
    reference = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)
    service_order = models.ForeignKey(
        'transactions.ServiceOrder',
        related_name='debit_notes',
        on_delete=models.CASCADE,
    )

    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Debit Note #{id} ({code})'.format(
            id=self.id,
            code=self.code
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.company = self.customer.company
        super().save(*args, **kwargs)

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(6)

    @property
    def total(self):
        total = self.debit_note_items.aggregate(
            total=Sum(
                F('price') * F('quantity'),
                output_field=DecimalField(),
            )
        )['total']
        return total or Decimal('0.0')


class DebitNoteItem(models.Model):
    debit_note = models.ForeignKey(
        'transactions.DebitNote',
        related_name='debit_note_items',
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    description = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unity_of_measure = models.CharField(max_length=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2, editable=False)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Debit Note Item #{id} Debit Note #({debit_note_code})'.format(
            id=self.id,
            debit_note_code=self.debit_note.code
        )

    def code(self):
        return f'{self.id:}'.zfill(6)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)
