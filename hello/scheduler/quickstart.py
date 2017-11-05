from __future__ import print_function
from apiclient import discovery
from httplib2 import Http

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from secret import credentials
from pprint import pformat

import base64
import datetime
import logging
import os
import re

try:
    from simplejson import loads, dumps
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    from json import loads, dumps
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
TOTAL_MONEY_SPENT = 0

def searchForEmail(service, query):
    total_money_spent = 0
    responses = service.users().messages().list(userId='me', q=query).execute()
    mesgs = responses['messages']
    for mes in mesgs:
        mesId = mes.get("id")
        resp = service.users().messages().get(userId='me', id=mesId).execute()
        messageStr = resp['snippet']
        dollars= re.findall("[0-9]+",messageStr)
        dollar = dollars[0]
        money = int(dollar)
        total_money_spent = money + total_money_spent

    return total_money_spent

def sendRequest(data, url, method):
    http = Http()
    resp, content = http.request(
        uri = url,
        method= method,
        headers={'Content-Type': 'application/json; charset=UTF-8'},
        body = dumps(data)
    )
    return resp, content

def sendMessageOnFb(message):
    print (message)
    PAGE_SECRET_TOKEN = os.environ['PAGE_SECRET_TOKEN']
    MY_SENDER_ID = os.environ['MY_SENDER_ID']

    dataObject = {
        "recipient": {
            "id": MY_SENDER_ID
        },
        "message": {
            "text": message
        }
    }

    url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + PAGE_SECRET_TOKEN
    resp, content = sendRequest(dataObject, url, 'POST')

    logging.info("Response dictionary")
    logging.info(pformat(resp))
    logging.info("Response Content Body")
    logging.info(pformat(content))


def getCurrentDate():
    return datetime.date.today()

def askForBiWeeklyBudget():
    msgDate = datetime.datetime(2017,10,21).date()
    currDate = getCurrentDate()
    if currDate == msgDate:
        sendMessageOnFb("Whats your budget for these 2 weeks?")

def main():
    creden = credentials.getCredentials()
    http = creden.authorize(Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    total_money_spent = searchForEmail(service, "subject:Large Transaction Warning")
    print (total_money_spent)

if __name__ == '__main__':
    main()