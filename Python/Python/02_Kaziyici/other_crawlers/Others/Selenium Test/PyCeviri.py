from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

gl_cvr = input("Lütfen yabancı kelimeyi giriniz: ")
class Ceviri:
        def __init__ (self):
            self.browser = webdriver.Chrome("chromedriver.exe")
        def transWord(self):
            self.browser.get("https://www.google.com.tr")
            self.browser.maximize_window()

            try:
                wordTrans = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")));
                wordTrans.send_keys("google translate")

            except:
                print("Hata oldu!")

            try:
                srchBtn = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")));
                srchBtn.click()

            except:
                prin("İnternet bağlantınızı kontrol ediniz!")

            try:
                wrdTrns = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='tw-source-text-ta']")));
                wrdTrns.send_keys(gl_cvr)  

            except:
                print("Hata!")

            try:
                Trnsword = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tw-tl']")));
                Trnsword.click()

            except:
                print("Bir hata meydana geldi!")

            try:
                detectLng = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tl_list-search-box']")));
                detectLng.send_keys("Turkish")
                detectLng.send_keys(Keys.ENTER)

            except:
                prin("Hata!")


trnsword = Ceviri()
trnsword.transWord()
