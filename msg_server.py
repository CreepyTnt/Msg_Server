import pytextnow
from duckduckgo_search import ddg
from duckduckgo_search import ddg_answers
import time
from datetime import datetime
# import html_downloader
# import validators
# import json

import msg_auth

client = pytextnow.Client(msg_auth.Username, sid_cookie=msg_auth.sid, csrf_cookie=msg_auth.csrf)

client.send_sms(msg_auth.test_num, 'server started') 

while True:
    time.sleep(3)
    new_messages = client.get_unread_messages()
    for message in new_messages:
        message.mark_as_read()
        print(message)  # message.content or message.number

        # if validators.url(message.content):
        #     html_downloader.download(message.content, 'C:/users/jenni/desktop/python/msg_thing/webpage.py')
        #     client.send_mms(message.number, 'C:/users/jenni/desktop/python/msg_thing/webpage.html')
        #     print ('sent a file')
        #     client.send_sms(message.number, 'Change the ".png" to ".html" to view')
        
        results = ddg(message.content, region='us-en', safesearch='moderate', time='y', max_results=5)

        answer = ddg_answers(message.content, related=False)

        try:
            client.send_sms(message.number, answer[0]['text'])

            time.sleep(0.1)
            
        except:  # update this, extreme PEP violation
            print('no ddg answer')
        

        client.send_sms(message.number, results[0]['title'] + '--------' + results[0]['body'] + '--------' + results[0]['href'])
        time.sleep(0.1)
        client.send_sms(message.number, results[1]['title'] + '--------' + results[1]['body'] + '--------' + results[1]['href'])
        time.sleep(0.1)
        client.send_sms(message.number, results[2]['title'] + '--------' + results[2]['body'] + '--------' + results[2]['href'])
        
        print(results)
        
        print(datetime.now())
        print()
