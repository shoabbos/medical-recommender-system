from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from . import patient, doctor


class rating_review(models.Model):
    patient = models.ForeignKey(patient ,null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(doctor ,null=True, on_delete=models.SET_NULL)
    
    rating = models.IntegerField(default=0)
    review = models.TextField( blank=True ) 

    @property
    def rating_is(self):
        new_rating = 0
        rating_obj = rating_review.objects.filter(doctor=self.doctor)
        for i in rating_obj:
            new_rating += i.rating
       
        new_rating = new_rating/len(rating_obj)
        new_rating = int(new_rating)
        
        return new_rating
