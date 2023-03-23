import pytextnow
from duckduckgo_search import ddg_answers
import time
from datetime import datetime


sid = 'connect_sid'
csrf = '_csrf'
phone_number = 'a valid cel or landline number (not textnow number)'
username = 'textnow username'

# Way 1. Include connect.sid and csrf cookie in the constructor
client = pytextnow.Client(username, sid_cookie = sid, csrf_cookie = csrf)
#client.auth_reset()

client.send_sms(phone_number, 'server started') 

while True:
    time.sleep(3)
    new_messages = client.get_unread_messages()
    for message in new_messages:
        message.mark_as_read()
        print(message) # message.content or message.number
        results = ddg_answers(message.content, related=False)
        client.send_sms(message.number, str(results))
        print (results)
        print ()
        print (datetime.timestamp)


