# Overview
An sms group chat and music downloader are in development. A website downloader and discord client may also be added soon.

* "msg_server_ddg_answers.py" is the server that searches things using duckduckgo answers.
* "msg_server_ddg_search.py" is the server software that searches thing with a standard duckduckgo search.
* "msg_server.py" is a revised server software that combines answers and search.
* "main.py" is a recently added file that implements all features in one place.


***Only run them one at a time, they are totally different server scripts and should not be used at the same time.***

Note: A feature of this service is that it can get "any" web page on the internet. While this is technically true, a
lot of websites don't like bots, so some won't work as expected. Selenium is a future possibility, as it can get html
data without being caught as well as take screenshots of the page, which will also eliminate the need for convertApi.



# Requirements:
### Modules:
*Note: Selenium and convertAPI can be used separately at your choice. See more on this below*
```
pip install pytextnow
pip install duckduckgo_search
pip install selenium
```
### Accounts:
You will need the following accounts:

* [TextNow](https://www.textnow.com/)
* [ConvertAPI (optional)](https://www.convertapi.com/)
# Selenium and ConvertAPI:
This code has the ability to get html data from web pages. To do this, you can use convertAPI or Selenium. Here is the
different benefits of the two:

* Selenium can render JavaScript and CSS data, whereas Requests cannot. Selenium also does not get caught as a bot, and
can take screenshots of the page. The only downside to using Selenium is the setup, which may be difficult, especially
if running code on a server.


* ConvertAPI is the alternative to Selenium. The downside is it cannot render JavaScript or CSS, will get caught as a
bot, and you have a limit. ConvertAPI is used to convert the HTML data to a .png file. This is done becuase TextNow
cannot send HTML files.

If you want to use selenium, set 'use_selenium' in msg_auth.py to True. Otherwise, set to False. (Shown below)

# Setup:

You will need to input your TextNow credentials into the *msg_auth.py* file. You will need the connect_sid and csrf cookie,
your TextNow username, and the number that is going to be used for testing (your main number).

* [How to get connect.sid and csrf cookie](https://github.com/leogomezz4t/PyTextNow_API/raw/main/get_cookie.mp4)
* [How to get TextNow username](https://github.com/leogomezz4t/PyTextNow_API/raw/main/get_username.mp4)

The following code shows where the credentials go:
```python
username = 'your_textnow_username'
sid = 'connect_sid_cookie'
csrf = 'csrf_token'

# this is your main phone number, not your TextNow number.
test_num = 'your_personal_phone_number'
```
**_ONLY IF_** you are using ConvertAPI will you need to use this key as well:
```python
# ConvertAPI key
convertapi_key = 'your_key'

# change this if you want to use ConvertAPI
use_selenium = True
```

After you have done this, you may run one of the files. If you are not sure which one to run, do main.py as that one
implements all features at once.

# Changelog
**1.4.0** = Searching now works the same way they did before v1.3.

**1.3.44** - Now uses Selenium headless mode.

**1.3.42** - You can now choose whether to use Selenium or ConvertAPI.

**1.3.4** - Now uses selenium.

**1.3.3** - Deletes the files after they are sent. The !webpage command is now stable.

**1.3.23** - Can now get any web page you specify

**1.3.2** - **beta** Can get web pages. TextNow cannot send html files, so it uses a free html to jpg converter

**1.3.1** - Added !help command to main.py

**1.3** - Added main.py. Includes all features in one file, and uses commands like !search

**1.2.8** - Minor bug fixes

**1.2.7** - Large amount of error correction and bug fixes in msg_server

**1.2.3** - Code cleanup, delete unnecessary __init __

**1.2.2** - Updated readme

**Second version** -  version uses a separate "auth" file for login and has duckduckgo answers and search in one.


# Coming Soon:
- group sms
- music downloader
- discord
