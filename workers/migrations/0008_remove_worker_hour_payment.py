# Generated by Django 3.1.4 on 2020-12-21 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0007_worker_hour_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='hour_payment',
        ),
    ]
