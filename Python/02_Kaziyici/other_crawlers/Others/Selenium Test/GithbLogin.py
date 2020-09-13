
from selenium import webdriver
#https://selenium-python.readthedocs.io/
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

gitname = ""
gitpass = ""

class Github:
        def __init__(self,gitname,gitpass):
            driver = "/home/can/Downloads/chromedriver"
            self.browser = webdriver.Chrome("chromedriver.exe")
            self.gitname = gitname
            self.gitpass = gitpass

        def singn(self):
            self.browser.get("https://github.com/login")
            self.browser.maximize_window()
            try:
                gitnameInput = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='login_field']")));
                gitpassInput = self.browser.find_element_by_xpath("//*[@id='password']")

                gitnameInput.send_keys(self.gitname)
                gitpassInput.send_keys(self.gitpass)
            except:
                print("Bir sorun oldu!")

            try:
                gitLgn = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='login']/form/div[3]/input[8]")));
                gitLgn.click()
            except:
                print("Bilinmeyen bir hata!")

githb = Github(gitname, gitpass)
githb.singn()
