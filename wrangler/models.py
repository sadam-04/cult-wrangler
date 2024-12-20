from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    times = models.JSONField()
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)

class EventResponse(models.Model):
    submitter = models.CharField(max_length=255)
    event_id = models.UUIDField()
    responses = models.JSONField()