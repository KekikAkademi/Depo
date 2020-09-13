from selenium import webdriver
from time import sleep

browser = webdriver.Chrome("chromedriver.exe")

browser.get("https://www.ayyildiz.org")

sleep(3)

pencere = browser.find_element_by_xpath('/html/body/div[10]/div/button')
pencere.click()

sleep(1)

icon_bas = browser.find_element_by_xpath('//*[@id="loginf"]')
icon_bas.click()

sleep(5)

username = browser.find_element_by_xpath('//*[@id="login_name"]')
password = browser.find_element_by_xpath('//*[@id="login_password"]')

sleep(2)

username.send_keys("HAYALETKOMANDO") #buraya adınızı
password.send_keys("")                      #buraya da şifrenizi girin

sleep(5)

giris = browser.find_element_by_xpath('//*[@id="loginpane"]/div/ul/li[3]/button/b')

giris.click()

sleep(20)

browser.close()