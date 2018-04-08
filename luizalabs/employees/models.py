from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255, help_text="Employee's name")
    email = models.EmailField(unique=True, help_text="A unique employee's email")
    departament = models.ForeignKey('Departament', on_delete=models.CASCADE, help_text="Employee's departament")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Departament(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
