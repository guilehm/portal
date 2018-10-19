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
