from rest_framework import serializers
from main.models import Employee, Departmen


class EmployeeSerializier(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class DepartmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departmen
        fields = "__all__"
