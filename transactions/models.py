from django.conf import settings
from django.db import models
from django.utils.functional import cached_property


class Event(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='events',
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        'register.Company',
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
    description = models.TextField()
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

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(6)

    def __str__(self):
        return 'Service Order #{id} ({subject})'.format(
            id=self.id,
            subject=self.subject
        )

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
