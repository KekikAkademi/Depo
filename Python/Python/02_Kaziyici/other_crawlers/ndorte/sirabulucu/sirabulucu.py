from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

keywords = {"example.com":["keyword 1", "keyword 2", "keyword 3"],
        "example1.com":["keyword 1", "keyword 2", "keyword 3"],
        "example2.com":["keyword 1", "keyword 2", "keyword 3"]}

for site in keywords:
    for keyword in keywords[site]:
        Find(keyword, site)

def Find(keyword, site):
    with open("user_agents.txt", "r") as agents:
        agent = random.choice(agents.readlines())
        a = agent.strip()
        agent = str(a)
        agents.close()
    caps = DesiredCapabilities.PHANTOMJS
    caps["phantomjs.page.settings.userAgent"] = agent
    driver = webdriver.PhantomJS("phantomjs.exe", desired_capabilities=caps)
    driver.set_window_size(1366, 768)
    url = ("https://www.google.com.tr/search?gl=&num=100&nfpr=1")
    driver.get(url)
    waitClick = random.randint(1, 3)
    sleep(waitClick)
    search = driver.find_element_by_name('q')
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)
    findKeyword = driver.find_elements_by_class_name("iUh30")
    count = 1
    for i in findKeyword:
        if site in i.text:
            print(site + " > " +keyword + " keyword found:  " + str(say) + ".")
            #driver.save_screenshot(keyword+".png") # if you take screenshot, erase #
        else:
            count += 1
    waitTime = random.randint(25, 35) #second
    sleep(waitTime)
    driver.quit()
