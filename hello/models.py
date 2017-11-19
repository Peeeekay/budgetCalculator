from django.db import models
import uuid
# Create your models here.

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

#important to keep track of new Emails
class Emails(models.Model):
	totalEmails = models.IntegerField()
	name = "DEFAULT"

#just stores the budget for 2 weeks.
class Budget(models.Model):
    budget = models.IntegerField()
    month = models.CharField(max_length=15)
    biWeekly = models.IntegerField()
    currDate = models.DateTimeField(auto_now_add=True)

