from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    school=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    skills=models.TextField(max_length=100)
    about_you=models.TextField(max_length=1000)
    previous_work=models.TextField(max_length=1000)


class PredResults(models.Model):

    Patient_ID = models.IntegerField()
    Patient_Age = models.IntegerField()
    Patient_Gender = models.IntegerField()
    Patient_Blood_Pressure = models.IntegerField()
    Patient_Heartrate = models.IntegerField()
    Heart_Disease = models.CharField(max_length=30)

    def __str__(self):
        return self.Heart_Disease