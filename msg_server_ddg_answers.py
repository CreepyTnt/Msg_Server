import pytextnow
from duckduckgo_search import ddg_answers
import time
from datetime import datetime
import msg_auth


# Way 1. Include connect.sid and csrf cookie in the constructor
client = pytextnow.Client(msg_auth.username, sid_cookie=msg_auth.sid, csrf_cookie=msg_auth.csrf)
# client.auth_reset()

client.send_sms(msg_auth.test_num, 'server started')

while True:
    time.sleep(3)
    new_messages = client.get_unread_messages()
    for message in new_messages:
        message.mark_as_read()
        print(message)  # message.content or message.number
        results = ddg_answers(message.content, related=False)
        client.send_sms(message.number, str(results))
        print(results)
        print()
        print(datetime.timestamp)
