# from hello.models import Emails
from django.db.models import F
from hello.scheduler.secret import credentials
from apscheduler.schedulers.background import BackgroundScheduler

import datetime


# def pollGmail(serivce):
#     query = 'subject:Large Transaction Warning'
#     emailIds = quickstart.searchForEmail(service, query)
#     totalNumberEmails = emailIds

#     emails = Emails.objects.get(name="DEFAULT")
#     if totalNumberEmails != emails.totalEmails:
#         emails.totalEmails = F('totalEmails') + totalNumberEmails
#         emails.save()
#         requestForNewEmails()

class Scheduler(object):
    def __init__(self):
        self.backGroundTask = BackgroundScheduler()

    def add_job(self,func,time,param=None):
        if param:
            self.backGroundTask.add_job(func, 'interval', seconds=time, args=[param])
        else:
            self.backGroundTask.add_job(func,'interval', seconds=time)

    def get_jobs(self):
        return self.backGroundTask.get_jobs()

    def start(self):
        self.backGroundTask.start()

