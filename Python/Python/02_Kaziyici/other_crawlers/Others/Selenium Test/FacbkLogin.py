from selenium import webdriver
#https://selenium-python.readthedocs.io/
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


mailname = ""
password1 = ""

class Facebook: #class ismini yazdık
    
    def __init__(self,mail,password): #self , mail ve password tanımladık
          self.browser = webdriver.Chrome("chromedriver.exe") #chrome yazarsak chromium üzerinden devam eder..
          self.mail = mailname
          self.password = password1

    def singIn(self): #ana işlemin gerçekleşeceği fonksiyon
          self.browser.get("https://www.facebook.com/login/") #işlemi gerçekleştirmek istediğimiz adres

          try:
            mailnameInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='email']")));
            password1Input = self.browser.find_element_by_xpath("//*[@id='pass']")

            mailnameInput.send_keys(self.mail) #mail ve şifremizi send_key() ile yazdırdık
            password1Input.send_keys(self.password)

          except:
            print("Bir hata oluştu!")
            
           try:
            fb_lgn = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='loginbutton']")));
            fb_lgn.clik()

           except:
            print("Bir hata meydana geldi!")
            
 facbk = Facebook(mailname,password1)
 facbk.singIn()
