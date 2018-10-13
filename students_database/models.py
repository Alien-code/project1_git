from django.db import models

# Create your models here.



class Guardian(models.Model):
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    GENDER_CHOICE = (('male', 'Male'), ('female', 'Female'))
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)
    age = models.IntegerField()
    phone = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICE = (('male', 'Male'), ('female', 'Female'))
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE)
    guard = models.OneToOneField(Guardian, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

