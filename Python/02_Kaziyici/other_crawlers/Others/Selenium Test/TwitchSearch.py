from selenium import webdriver


tw_ans = input("Enter a name of stramer: ").title()

class Twitch:
    def __init__(self):
            self.browser = webdriver.Chrome("chromedriver.exe")


    def searchTwtch(self):
        self.browser.get("https://www.twitch.tv/" + tw_ans)
        self.browser.maximize_window()
      
       

twitchSearch = Twitch()
twitchSearch.searchTwtch()

