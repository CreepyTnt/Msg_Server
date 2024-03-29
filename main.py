import convertapi
import pytextnow
import requests
from duckduckgo_search import ddg
from duckduckgo_search import ddg_answers
from selenium.webdriver.chrome.options import Options
import Custom_Message_Protocols as sms
import msg_auth
import time
import os
from selenium import webdriver

def search(query):
    results = ddg(message.content, region='us-en', safesearch='moderate', time='y', max_results=5)

    answer = ddg_answers(message.content, related=False)

    try:
        client.send_sms(message.number, answer[0]['text'])

        time.sleep(3)
            
    except:
        print ('no ddg answer')
        

    client.send_sms(message.number, results[0]['title'] + '--------' + results[0]['body'] + '--------' + results[0]['href'])
    time.sleep(3)
    client.send_sms(message.number, results[1]['title'] + '--------' + results[1]['body'] + '--------' + results[1]['href'])
    time.sleep(3)
    client.send_sms(message.number, results[2]['title'] + '--------' + results[2]['body'] + '--------' + results[2]['href'])



def answers(msg):

    user_response = sms.ask("Input prompt.", msg)

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

    if msg_auth.use_selenium is True:

        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-startup-window")

        window_size = "1920,1080"
        chrome_options.add_argument(f"--window-size={window_size}")

        driver = webdriver.Chrome(options=chrome_options)

        driver.get(user_response)
        with open("file.png", 'wb') as f:
            f.write(driver.get_screenshot_as_png())

        msg.send_mms("file.png")

        os.remove("file.png")

    else:

        r = requests.get(user_response)
        with open("file.html", "w") as f:
            f.write(r.text)

        convertapi.api_secret = convertapi_key
        convertapi.convert('jpg', {
            'File': 'file.html'
        }, from_format='html').save_files('file2.jpg')

        message.send_mms("file2.jpg")

        os.remove("file2.jpg")
        os.remove('file.html')


client = pytextnow.Client(msg_auth.username, sid_cookie=msg_auth.sid, csrf_cookie=msg_auth.csrf)
client.send_sms(msg_auth.test_num, 'Server started.')
print("Server started.")

# 0 = search
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

                print(f"{message.number}: {message.content}")
                answers(message)

            elif str.lower(message.content) == "!help":

                print(f"{message.number}: {message.content}")
                message.send_sms("Current commands: !webpage and !help. To simply search, just send you query without !.")

            elif str.lower(message.content) == "!web" or str.lower(message.content) == "!webpage":

                print(f"{message.number}: {message.content}")
                webpage(message)

            else:
                valid = 1
                message.send_sms(f"Invalid command '{message.content}'. Say !help for a list of commands.")

        else:
            valid = 0

            print(f"{message.number}: {message.content}")
            search(message.content)



        if valid == 1:
            print(f"{message.number}: {message.content} (invalid-notified user)")
        elif valid == 0:
            print(f"{message.number}: {message.content} (search query)")
