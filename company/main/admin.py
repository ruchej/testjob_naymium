from django.contrib import admin
from .models import Employee, Departmen


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ("fio", "departmen", "position")
    search_fields = ("fio",)


@admin.register(Departmen)
class DepartmenAdmin(admin.ModelAdmin):

    list_display = ("name", "director")
