from django_filters.rest_framework import FilterSet

from main.models import Employee


class EmployeeFilter(FilterSet):
    class Meta:
        model = Employee
        fields = ("fio", "departmen")
