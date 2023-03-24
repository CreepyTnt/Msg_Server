import pytextnow
from duckduckgo_search import ddg
import time
from datetime import datetime
import msg_auth
import Custom_Message_Protocols as sms


client = pytextnow.Client(msg_auth.username, sid_cookie=msg_auth.sid, csrf_cookie=msg_auth.csrf)


client.send_sms(msg_auth.test_num, 'Server started.')


while True:
    time.sleep(3)
    new_messages = client.get_unread_messages()
    for message in new_messages:
        message.mark_as_read()

        print(message)  # message.content or message.number
        results = ddg(message.content, region='us-en', safesearch='moderate', time='y', max_results=3)
        sms.send_sms(str(results), message)
        print(results)
        
        
        print(datetime.now())
        print()
