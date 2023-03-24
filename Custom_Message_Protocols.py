import time
from pytextnow import Client
import msg_auth


def send_sms(content, msg, debug=False):
    # This is used when a long message is possible to be sent
    # also used cuz pytextnow does not like certain characters

    sms_limit = 1500
    i = 0

    # pytextnow does not support these characters

    content = content.replace("\n", '      ')
    content = content.replace('"', "'")

    list_response = [content[i:i + sms_limit] for i in
                     range(0, len(content), sms_limit)]

    for message in list_response:

        if 1 < len(list_response) != i:
            if debug: print(message + "...")
            msg.send_sms(message + "...")

        else:
            if debug: print(message)
            msg.send_sms(message)

        time.sleep(8)
        i += 1


def ask(question, msg, timeout=60, default="", advanced=False):
    client = Client(msg_auth.username, sid_cookie=msg_auth.sid, csrf_cookie=msg_auth.csrf)

    timer_timeout = time.perf_counter()
    msg.send_sms(question)

    while time.perf_counter() - timer_timeout <= timeout:
        time.sleep(1)
        new_messages = client.get_unread_messages()

        for message in new_messages:

            if message.number == msg.number:
                message.mark_as_read()
                if advanced:
                    return message
                else:
                    return message.content

    # timeout error messages

    time.sleep(1)
    if default != "":
        msg.send_sms(f'ERROR:TIMEOUT. User took too long to respond. Default response: {default}.')
    else:
        msg.send_sms("ERROR:TIMEOUT. User took too long to respond. Please use command again to retry.")

    return default
