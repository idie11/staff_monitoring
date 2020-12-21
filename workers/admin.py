from django.contrib import admin
from . import models


class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'worker_id', 
        'get_full_name', 
        'salary_type',
        'position',
        'worked_hours',
        'salary',
        'count_of_sales',
        'phone',
        'email',
        'week_salary',
        'productivity',
        'total'
    )

    def get_full_name(self, obj):
        return f'{obj.name} {obj.second_name}'

    def week_salary(self, obj):
        position = obj.position
        
        if position == 'Менеджер' or position == 'Секретарь':
            return obj.salary / 4
        elif position == 'Работник цеха' or position == 'Секретарь на замену':
            return obj.salary * obj.worked_hours
        elif position == 'Продавец':
            return (obj.salary / 4) + (obj.count_of_sales * 50)
    
    def productivity(self, obj):
        worked_hours = obj.worked_hours

        if worked_hours >= 34:
            return 'Лучший сотрудник'
        elif worked_hours >= 28 and worked_hours < 34:
            return 'Хороший сотрудник'
        elif worked_hours < 28:
            return 'Плохой сотрудник'

    def total(self, obj):
        workers = models.Worker.objects.all()
        total_salary = 0

        for i in workers:
            if i.position == 'Менеджер' or i.position == 'Секретарь':
                total_salary += (i.salary / 4)
            elif i.position == 'Работник цеха' or i.position == 'Секретарь на замену':
                total_salary += (i.salary * i.worked_hours)
            elif i.position == 'Продавец':
                total_salary += (i.salary / 4) + (i.count_of_sales * 50)

        return total_salary

admin.site.register(models.Worker, WorkerAdmin)
