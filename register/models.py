from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property


class MainCompany(models.Model):
    name = models.CharField(max_length=50)
    commercial_name = models.CharField(max_length=100, blank=True, null=True)
    registered_number = models.CharField(max_length=20, unique=True, db_index=True, null=True, blank=True)
    email = models.EmailField(max_length=200, db_index=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=100, unique=True, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    address = models.ForeignKey(
        'register.Address',
        related_name='entities',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    logo_thumb = models.ImageField(
        null=True,
        blank=True,
        upload_to='register/maincompany/logothumb',
    )
    logo = models.ImageField(
        null=True,
        blank=True,
        upload_to='register/maincompany/logo',
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'main company'

    def __str__(self):
        return self.name

    def clean(self):
        if MainCompany.objects.exists() and not self.pk:
            raise ValidationError('Only one main company is allowed')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=50)
    commercial_name = models.CharField(max_length=100, blank=True, null=True)
    registered_number = models.CharField(max_length=20, unique=True, db_index=True, null=True, blank=True)
    email = models.EmailField(max_length=200, db_index=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=100, unique=True, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    address = models.ForeignKey(
        'register.Address',
        related_name='companies',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Machine(models.Model):
    code = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True, unique=True, db_index=True)
    active = models.BooleanField(default=True, db_index=True)
    company = models.ForeignKey(
        'register.Company',
        related_name='machines',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    date_sale = models.DateField(blank=True, null=True)
    date_warranty = models.DateField(blank=True, null=True)
    date_setup = models.DateField(blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return 'Machine #{id} ({code})'.format(
            id=self.id,
            code=self.code
        )


class Worker(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    active = models.BooleanField(default=True, db_index=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(3)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Category(models.Model):
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True, db_index=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(3)

    class Meta:
        verbose_name_plural = 'Categories'


class Message(models.Model):
    message = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_message

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(3)

    @property
    def short_message(self):
        return '{short_message}...'.format(
            short_message=self.message[:50]
        )


class Address(models.Model):
    postal_code = models.CharField(max_length=10, blank=True, null=True, db_index=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    complement = models.CharField(max_length=20, null=True, blank=True)
    district = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=2, blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Address #{id} ({address})'.format(
            id=self.id,
            address=self.address or ''
        )

    class Meta:
        verbose_name_plural = 'addresses'


class User(AbstractUser):
    company = models.ForeignKey(
        'register.Company',
        related_name='users',
        on_delete=models.CASCADE,
        null=True,
    )
    doc = models.CharField(max_length=20, null=True, blank=True, db_index=True, unique=True)
    home_phone_number = models.CharField(max_length=20, null=True, blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True, blank=True)
    work_phone_number = models.CharField(max_length=20, null=True, blank=True)
    woeid = models.CharField(max_length=20, null=True, blank=True)
    address = models.ForeignKey(
        'register.Address',
        related_name='users',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    @property
    def phone_number(self):
        return self.cell_phone_number or self.home_phone_number or self.work_phone_number or ''

    @cached_property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
