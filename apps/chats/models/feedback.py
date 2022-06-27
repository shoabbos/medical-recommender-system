from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __unicode__(self):
        return self.feedback
