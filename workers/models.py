from django.db import models


SALARY_TYPE = [
    ('Фиксированная заработная плата', 'Фиксированная заработная плата'),
    ('Заработная плата + комиссионные', 'Заработная плата + комиссионные'),
    ('Почасовой оклад', 'Почасовой оклад')
]

POSITIONS = [
    ('Менеджер', 'Менеджер'),
    ('Секретарь', 'Секретарь'),
    ('Секретарь на замену', 'Секретарь на замену'),
    ('Продавец', 'Продавец'),
    ('Работник цеха', 'Работник цеха'),
]


class Worker(models.Model):
    worker_id = models.IntegerField(unique=True, verbose_name='ID сотрудника')
    name = models.CharField(max_length=24, verbose_name='Имя сотрудника')
    second_name = models.CharField(max_length=24, verbose_name='Фамилия сотрудника')
    salary_type = models.CharField(max_length=120, choices=SALARY_TYPE, verbose_name='Вид заработной платы')
    position = models.CharField(max_length=120, choices=POSITIONS, verbose_name='Должность')
    worked_hours = models.IntegerField(verbose_name='Отработано часов в неделю')
    salary = models.IntegerField(verbose_name='Заработная плата', blank=True, null=True)
    count_of_sales = models.IntegerField(verbose_name='Количество продаж', null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Адрес электронной почты')
    
    def __str__(self):
        return f'{self.name} {self.second_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    