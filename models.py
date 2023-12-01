from django.db import models

from django.db import models

class Admin(models.Model):
    a_id = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=255)

class Employee(models.Model):
    e_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    phno = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    sal_package = models.DecimalField(max_digits=10, decimal_places=2)

class Member(models.Model):
    m_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    phno = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    e_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    current_package = models.CharField(max_length=255)  

