from django.db import models
from django.contrib.auth.models import User
from apps.main_app.models import consultation


class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    consultation_id =  models.ForeignKey(consultation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __unicode__(self):
        return self.message
