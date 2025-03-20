from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):
    patientname = models.CharField(max_length=100)
    patientage = models.IntegerField()
    patientgender = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    doctorname = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.patientname} - {self.date} {self.time}"


class Doctor(models.Model):
    doctorname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="images/")
    detailshtml = models.CharField(max_length=100)

    def __str__(self):
        return self.doctorname
