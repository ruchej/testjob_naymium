from django.db import models
from django.db.models import Sum, Count


class Employee(models.Model):

    fio = models.CharField(max_length=255, db_index=True, verbose_name="ФИО")
    photo = models.ImageField(upload_to="img", blank=True, verbose_name="Фото")
    position = models.CharField(max_length=100, verbose_name="Должность")
    salary = models.DecimalField(
        max_digits=9, decimal_places=2, default=0, verbose_name="Оклад"
    )
    age = models.PositiveSmallIntegerField(default=0, verbose_name="Возраст")
    departmen = models.ForeignKey(
        "Departmen", on_delete=models.CASCADE, verbose_name="Департамент"
    )

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "Сотрудники"
        unique_together = ("fio", "departmen")

    def __str__(self):
        return self.fio


class Departmen(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название")
    director = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="employee",
        blank=True,
        null=True,
        verbose_name="Директор",
    )

    class Meta:
        verbose_name = "департамент"
        verbose_name_plural = "Департаменты"

    def __str__(self):
        return self.name

    def get_sum_salary(self):
        """Вернуть сумму окладов сотрудников данного департамента"""
        return (
            self.employee_set.filter(departmen=self.pk).aggregate(Sum("salary"))[
                "salary__sum"
            ]
            or 0
        )

    def get_count_employee(self):
        return (
            self.employee_set.filter(departmen=self.pk).count()
            or 0
        )