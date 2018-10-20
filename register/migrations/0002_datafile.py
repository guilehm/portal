# Generated by Django 2.1.2 on 2018-10-21 01:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='register/datafile/file')),
                ('original_file_name', models.CharField(blank=True, max_length=500, null=True)),
                ('extension', models.CharField(blank=True, max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]