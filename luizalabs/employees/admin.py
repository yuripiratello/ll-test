from django.contrib import admin

from employees.models import Employee, Departament

admin.site.site_header = 'Luizalabs Employee Manager'


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'departament']
    list_filter = ['departament']
    search_fields = ['name', 'email', 'departament__name']
