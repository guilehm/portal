# Generated by Django 2.1.2 on 2018-10-21 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='register.Category')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='register.Machine')),
                ('pictures', models.ManyToManyField(related_name='events', to='register.Picture')),
            ],
        ),
    ]