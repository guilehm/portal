from django.db import models
from django.utils.functional import cached_property


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
        related_name='entities',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


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
        return f'{self.id:}'.zfill(6)

    @cached_property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @cached_property
    def phone_number(self):
        return self.cell_phone_number or self.home_phone_number or ''


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
    title = models.CharField(max_length=100)
    message = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @cached_property
    def code(self):
        return f'{self.id:}'.zfill(3)

    @property
    def short_message(self):
        return '{short_message}...'.format(
            short_message=self.message[:10]
        )


class Picture(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(
        upload_to='register/picture/image'
    )

    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return 'Picture #{id} ({title})'.format(
            id=self.id,
            title=self.title or 'Untitled'
        )
