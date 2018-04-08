from django.contrib import admin

from employees.models import Employee, Departament


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'departament']
    list_filter = ['departament']
