# Generated by Django 2.1.2 on 2018-10-19 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]