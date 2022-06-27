from django.db import models

from . import patient, doctor, diseaseinfo


class consultation(models.Model):

    patient = models.ForeignKey(patient ,null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(doctor ,null=True, on_delete=models.SET_NULL)
    diseaseinfo = models.OneToOneField(diseaseinfo, null=True, on_delete=models.SET_NULL)
    consultation_date = models.DateField()
    status = models.CharField(max_length = 20)
