from apscheduler.schedulers.background import BackgroundScheduler
import quickstart
import datetime

def pollGmail(serivce):
    query = 'subject:Large Transaction Warning'
    emailIds = quickstart.totalEmails(service, query)
    totalNumberEmails = emailIds


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

if __name__ =="__main__":
    sch = Scheduler()
    sch.start()
    credentials=quickstart.get_credentials()
    http = credentials.authorize(Http())
    service = discovery.build('gmail', 'v1', http=http)

    sch.add_job(pollGmail, 30, service)

    while(True):
        pass
