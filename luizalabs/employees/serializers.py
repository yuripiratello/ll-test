from rest_framework import serializers

from employees.models import Employee


class EmployeePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'departament')


class EmployeeGETSerializer(EmployeePOSTSerializer):
    departament = serializers.StringRelatedField(many=False)
