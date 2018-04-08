from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers import EmployeePOSTSerializer, EmployeeGETSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    create:
    Create new employee

    read:
    Retrieve a employee

    delete:
    Delete a employee

    """
    authentication_classes = []
    permission_classes = []
    http_method_names = ['get', 'post', 'delete']
    queryset = Employee.objects.all()
    serializer_class = EmployeeGETSerializer

    def get_serializer_class(self):
        assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
        )

        print(self.action)

        if self.action in ('create', 'update'):
            return EmployeePOSTSerializer
        else:
            return self.serializer_class
