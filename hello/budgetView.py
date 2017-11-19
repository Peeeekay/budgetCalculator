from .models import Budget, Emails
from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json
import os
import re

import hello.scheduler.quickstart as quick

def parseBudget(mes):
    amounts = re.findall("[0-9]+", mes)
    return int(amounts[0])

def sendReply(reply):
    quick.sendMessageOnFb(reply)

def setBudget(mesg):
    budget = parseBudget(mesg)
    b=Budget(budget = budget, month="NOVEMBER", biWeekly = 2)
    b.save()

    reply = formt("Your budget: %s for month: %s has been saved for 2 weeks.", budget, "NOVEMBER")
    sendReply(reply)

def getExpense():
    pass

def switchString(arg):
    if "SBUDGET" in arg:
        setBudget(arg)
    elif "GEXPENSE" in arg:
        getExpense()

def doAction(message):
    """ Does all the cool stuff """
    pass

class BudgetView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == os.environ['VERIFY_TOKEN']:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events
                if 'message' in message:
                    # Print the message to the terminal
                    mesg = message['message']
                    print (message)
                    if "text" not in mesg.keys():
                        print("not a vaild text")
                    else:
                        txt = mesg["text"]
                        switchString(txt)
        return HttpResponse()