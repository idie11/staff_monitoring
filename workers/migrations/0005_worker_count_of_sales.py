# Generated by Django 3.1.4 on 2020-12-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0004_worker_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='count_of_sales',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество продаж'),
        ),
    ]
