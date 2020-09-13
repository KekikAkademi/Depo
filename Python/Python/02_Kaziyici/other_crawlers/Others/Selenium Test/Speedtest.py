from selenium import webdriver
#https://selenium-python.readthedocs.io/
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Speed:
        def __init__(self):
            self.browser = webdriver.Chrome("chromedriver.exe")
            

        def pressButon(self):
            self.browser.get("https://www.speedtest.net/")
#           self.browser.maximize_window()
            try:
                butonPress = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='container']/div[2]/div/div/div/div[2]/div[3]/div[1]/a")));
                butonPress.click()

            except:
                print("Bir hata oluştu!")

sped = Speed()
sped.pressButon()
