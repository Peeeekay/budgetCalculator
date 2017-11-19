from apscheduler.schedulers.background import BackgroundScheduler
from hello.scheduler.secret import credentials
from hello.scheduler.apScheduler import Scheduler

import hello.helper as helper
import datetime

from apiclient import discovery
from httplib2 import Http  
 
if __name__ =="__main__":
    sch = Scheduler()
    sch.start()
    creden=credentials.getCredentials()
    http = creden.authorize(Http())
    service = discovery.build('gmail', 'v1', http=http)

    sch.add_job(helper.pollGmail, 2, service)

    while(True):
        pass
