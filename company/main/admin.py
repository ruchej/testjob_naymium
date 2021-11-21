from django.contrib import admin
from .models import Employee, Departmen


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ("fio", "departmen", "position", "salary")
    search_fields = ("fio",)


@admin.register(Departmen)
class DepartmenAdmin(admin.ModelAdmin):

    list_display = ("name", "director", "get_sum_salary", "get_count_employee")
    read_only_fields = ("get_sum_salary", "get_count_employee")
