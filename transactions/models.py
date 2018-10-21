from django.db import models


class Event(models.Model):
    # TODO: ForeignKey to Customer
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
        'register.Picture',
        related_name='events',
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)


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
    # TODO: ForeignKey to Customer
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
        'register.Picture',
        related_name='service_orders',
    )
