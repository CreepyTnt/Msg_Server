import time


# This is used when a long message is possible to be sent
# also used cuz pytextnow does not like certain characters
def send_sms(content, msg):
    sms_limit = 550

    # pytextnow does not support these characters
    content = content.replace("\n", '      ')
    content = content.replace('"', '*')

    list_response = [content[i:i + sms_limit] for i in
                     range(0, len(content), sms_limit)]

    for message in list_response:
        msg.send_sms(message)
        time.sleep(3)
