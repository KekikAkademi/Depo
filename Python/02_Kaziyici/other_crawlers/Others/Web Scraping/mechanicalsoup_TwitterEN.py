## https://piratefache.ch/python-3-mechanize-and-beautifulsoup/

import mechanicalsoup # Don’t forget to import the new module

if __name__ == "__main__":

    URL = "https://twitter.com/login"
    LOGIN = "your_login"
    PASSWORD = "your_password"
    TWITTER_NAME = "displayed_name" # Displayed username on Twitter

    # Create a browser object
    browser = mechanicalsoup.StatefulBrowser()

    # request Twitter login page
    browser.open(URL)

    # we grab the login form
    browser.select_form('form[action="https://twitter.com/sessions"]')

    # print form inputs
    browser.get_current_form().print_summary()

    # specify username and password
    browser["session[username_or_email]"] = LOGIN
    browser["session[password]"] = PASSWORD

    # submit form
    response = browser.submit_selected()

    # get current page output
    response_after_login = browser.get_current_page()

    # verify we are now logged in ( get img alt element containing username )
    # if you found a better way to check, let me know. Since twitter generate dynamically all theirs classes, its
    # pretty complicated to get better information
    user_element = response_after_login.select_one("img[alt="+TWITTER_NAME+"]")

    # if username is in the img field, it means the user is successfully connected
    if TWITTER_NAME in str(user_element):
        print("You're connected as " + TWITTER_NAME)
    else:
        print("Not connected")