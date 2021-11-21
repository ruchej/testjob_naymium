from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EmployeeSerializier, DepartmenSerializer
from .filters import EmployeeFilter
from main.models import Employee, Departmen


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


class EmployeeViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializier
    filter_class = EmployeeFilter
    pagination_class = StandardResultsSetPagination


class DepartmenViewSet(viewsets.ModelViewSet):

    queryset = Departmen.objects.all()
    serializer_class = DepartmenSerializer
