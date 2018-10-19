# Generated by Django 2.1.2 on 2018-10-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='register/picture/image')),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_changed', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
