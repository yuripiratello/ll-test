from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient
from employees.models import Employee
from employees.serializers import EmployeeGETSerializer


class TestEmpoyleeView(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Yuri Piratello",
            email="yuri@luizalabs.com",
            departament_id=1
        )
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def test_success_get_employee(self):
        response = self.client.get(reverse('employee-detail', kwargs={'pk': self.employee.pk}))
        serializer = EmployeeGETSerializer(self.employee, )
        self.assertEquals(response.data, serializer.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_success_get_employees(self):
        response = self.client.get(reverse('employee-list'))
        employees = Employee.objects.all()
        serializer = EmployeeGETSerializer(employees, many=True)
        self.assertEquals(response.data, serializer.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_employees(self):
        delete = self.client.delete(reverse('employee-destroy', kwargs={'pk': self.employee.pk}))
        self.assertEquals(delete.status_code, status.HTTP_204_NO_CONTENT)
        not_found = self.client.get(reverse('employee-detail', kwargs={'pk': self.employee.pk}))
        self.assertEquals(not_found.status_code, status.HTTP_404_NOT_FOUND)
