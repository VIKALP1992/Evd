from django.db import models
class Employee(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    email=models.EmailField(max_length=40)
    address=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
