from django.db import models

# Create your models here.
class SchoollInfo(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.IntegerField()
    district = models.CharField(max_length=100)
    address = models.TextField()
    stablished_date = models.DateField()

    def __str__(self):
        return self.name
