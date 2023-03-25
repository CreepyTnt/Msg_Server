import pytextnow
from duckduckgo_search import ddg_answers, ddg
import Custom_Message_Protocols as sms
import msg_auth
import time
import requests
import convertapi
import os


def answers(msg):

    user_response = sms.ask("Input prompt.", msg)

    # if validators.url(message.content):
    #     html_downloader.download(message.content, 'C:/users/jenni/desktop/python/msg_thing/webpage.py')
    #     client.send_mms(message.number, 'C:/users/jenni/desktop/python/msg_thing/webpage.html')
    #     print ('sent a file')
    #     client.send_sms(message.number, 'Change the ".png" to ".html" to view')

    # get duckduckgo responses

    results = ddg(user_response, region='us-en', safesearch='moderate', time='y', max_results=3)
    answer = ddg_answers(user_response, related=False)

    try:

        # send simple search

        sms.send_sms("Explanation: " + answer[0]['text'], msg, debug=True)

        # send detailed search

        response = ""
        for i in range(3):
            response += f"Result {i + 1}: {results[i]['title']}-'{results[i]['href']}. Body: {results[i]['body']}   "

        sms.send_sms(response, msg, debug=True)

    except IndexError:
        msg.send_sms("There was an error: INDEX_ERROR. This is most likely caused because of no response from DuckDuckGo.")


def webpage(msg):
    user_response = sms.ask("Respond with the url of your webpage. Remember to put https:// before it.", msg, default="https://google.com")

    r = requests.get(user_response)
    with open("file.html", "w") as f:
        f.write(r.text)

    convertapi.api_secret = convertapi_key
    convertapi.convert('jpg', {
        'File': 'file.html'
    }, from_format='html').save_files('file2.jpg')

    message.send_mms("file2.jpg")

    os.remove("file.html")
    os.remove("file2.jpg")




client = pytextnow.Client(msg_auth.username, sid_cookie=msg_auth.sid, csrf_cookie=msg_auth.csrf)
client.send_sms(msg_auth.test_num, 'Server started.')

# 0 = not valid
# 1 = invalid command
# 2 = valid
valid = 0

convertapi_key = msg_auth.convertapi_key



while True:

    time.sleep(3)
    messages = client.get_unread_messages()

    for message in messages:

        message.mark_as_read()
        valid = 2

        if str.lower(message.content)[0] == "!":

            if str.lower(message.content) == "!search":
                answers(message)

            elif str.lower(message.content) == "!help":
                message.send_sms("Current commands: !search, !help.")

            elif str.lower(message.content) == "!web":
                webpage(message)

            else:
                valid = 1
                message.send_sms(f"Invalid command '{message.content}'. Say !help for a list of commands.")

        else:
            valid = 0

        if valid == 2:
            print(f"{message.number}: {message.content}")
        elif valid == 1:
            print(f"{message.number}: {message.content} (invalid-notified user)")
        else:
            print(f"{message.number}: {message.content} (invalid)")



