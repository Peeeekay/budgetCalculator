from django.db import models
import uuid
# Create your models here.

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Jobs(models.Model):
    name = models.CharField(max_length=30)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False)

class Budget(models.Model):
    budget = models.IntegerField()
    month = models.CharField(max_length=15)
    biWeekly = models.IntegerField()
    currDate = models.DateTimeField(auto_now_add=True)

