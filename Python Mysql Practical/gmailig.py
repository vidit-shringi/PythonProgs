from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

creds = Credentials.from_authorized_user_file('path/to/credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
service = build('gmail', 'v1', credentials=creds)

result = service.users().messages().list(userId='me', maxResults=10).execute()
messages = result.get('messages', [])

for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    print(msg['snippet'])
