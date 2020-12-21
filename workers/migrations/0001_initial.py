# Generated by Django 3.1.4 on 2020-12-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_id', models.IntegerField(unique=True, verbose_name='ID сотрудника')),
                ('name', models.CharField(max_length=24, verbose_name='Имя сотрудника')),
                ('second_name', models.CharField(max_length=24, verbose_name='Фамилия сотрудника')),
                ('salary_type', models.CharField(choices=[('Фиксированная заработная плата', 'Фиксированная заработная плата'), ('Заработная плата + комиссионные', 'Заработная плата + комиссионные'), ('Почасовой оклад', 'Почасовой оклад')], max_length=120)),
                ('position', models.CharField(choices=[('Менеджер', 'Менеджер'), ('Секретарь', 'Секретарь'), ('Продавец', 'Продавец'), ('Работник цеха', 'Работник цеха')], max_length=120)),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]