import os
from os.path import join, dirname

from twilio.rest import TwilioRestClient 
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

auth = os.environ.get('TWILIO_SID')
token = os.environ.get('TWILIO_SECRET')

client = TwilioRestClient(auth,token)  
msg = client.messages.create(to='', from_='', body="test")