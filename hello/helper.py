# from hello.models import Email
from django.db.models import F
import hello.scheduler.quickstart as gmail 

# def pollGmail(serivce):
#     query = 'subject:Large Transaction Warning'
#     emailIds = quickstart.searchForEmail(service, query)
#     totalNumberEmails = emailIds

#     emails = Emails.objects.get(name="DEFAULT")
#     if totalNumberEmails != emails.totalEmails:
#         emails.totalEmails = F('totalEmails') + totalNumberEmails
#         emails.save()
#         requestForNewEmails()

def pollGmail(service):
	
	query = "subject:Large Transaction Warning after:2017/08/14"

	try:
		emails = gmail.searchForEmail(service, query)

		print("---------***----------")
		print(emails)
		print("---------***----------")
	except Exception as e:
		print(e)
