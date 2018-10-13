from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    teacher_id = models.IntegerField()
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name, self.department
