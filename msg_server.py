import pytextnow
from duckduckgo_search import ddg
from duckduckgo_search import ddg_answers
import time
from datetime import datetime
# import html_downloader
# import validators
# import json
import Custom_Message_Protocols as sms
import msg_auth

client = pytextnow.Client(msg_auth.username, sid_cookie=msg_auth.sid, csrf_cookie=msg_auth.csrf)

client.send_sms(msg_auth.test_num, 'Server started.')

while True:
    time.sleep(3)
    messages = client.get_unread_messages()
    for message in messages:

        message.mark_as_read()
        print(f"{message.number}: {message.content}")

        # if validators.url(message.content):
        #     html_downloader.download(message.content, 'C:/users/jenni/desktop/python/msg_thing/webpage.py')
        #     client.send_mms(message.number, 'C:/users/jenni/desktop/python/msg_thing/webpage.html')
        #     print ('sent a file')
        #     client.send_sms(message.number, 'Change the ".png" to ".html" to view')

        # get duckduckgo responses

        results = ddg("message.content", region='us-en', safesearch='moderate', time='y', max_results=5)
        answer = ddg_answers(message.content, related=False)

        # send simple search

        print(answer[0]['text'])
        sms.send_sms(answer[0]['text'], message)

        # send detailed search

        sms.send_sms(results[0]['title'] + '--------' + results[0]['body'] + '--------' + results[0]['href'], message)
        time.sleep(3)
        sms.send_sms(results[1]['title'] + '--------' + results[1]['body'] + '--------' + results[1]['href'], message)
        time.sleep(3)
        sms.send_sms(results[2]['title'] + '--------' + results[2]['body'] + '--------' + results[2]['href'], message)



        print(results)
        print(datetime.now())
        print()
