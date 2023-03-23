# Overview
If you want to host the server yourself here is everything you need to know. A website downloader, music downloader,
and discord client may also be added soon.

* "msg_server_ddg_answers.py" is the server that searches things using duckduckgo answers.
* "msg_server_ddg_search.py" is the server software that searches thing with a standard duckduckgo search.
* "msg_server.py" is a revised server software that combines answers and search.


***Only run them one at a time, they are totally different server scripts and should not be used at the same time.***



# Requirements:
### Modules:
```
pip install pytextnow
pip install duckduckgo_search
```
### Accounts:
You will need the following accounts:

* [TextNow](https://www.textnow.com/)

# Setup:

You will need to input your credentials into the *msg_auth.py* file. You will need the connect_sid and csrf cookie,
your TextNow username, and the number that is going to be used for testing (your main number).

* [How to get connect.sid and csrf cookie](https://github.com/leogomezz4t/PyTextNow_API/raw/main/get_cookie.mp4)
* [How to get TextNow username](https://github.com/leogomezz4t/PyTextNow_API/raw/main/get_username.mp4)

The following code shows where the credentials go:
```python
Username = 'your_textnow_username'
sid = 'connect_sid_cookie'
csrf = 'csrf_token'

# this is your main phone number, not your TextNow number.
test_num = 'your_personal_phone_number'
```

# Changelog
**1.21** - Updated readme

**Second version** -  version uses a separate "auth" file for login and has duckduckgo answers and search in one.
