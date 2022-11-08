from __future__ import print_function
from email.mime import base

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def VerifyEmail(email = 'verifymesenpai69+maddy@gmail.com', fromAddress = 'noreply@clickasnap.com'):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me',labelIds=['INBOX']).execute()
        labels = results.get('messages', [])

        if not labels:
            print('No messages found.')
            return
        print('Messages: ' + str(len(labels)))
        for message in labels:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            deliveredAddress = msg['payload']['headers'][0]['value']
            sentAddress = msg['payload']['headers'][14]['value']
            
            if(fromAddress in sentAddress) and (str(deliveredAddress).upper() == str(email).upper()):
                messageString = base64.urlsafe_b64decode(msg['payload']['body']['data'])
                parsedMessageString = str(messageString).split('Thank you for registering with ClickASnap.<br /><br />Please click the link below to activate your membership.<br /><br /><a href="')[1]
                parsedMessageString = str(parsedMessageString).split('" target=')[0]
                print(parsedMessageString)
                print('CORRECT EMAIL')

                return parsedMessageString

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')