from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


usrnm = ""
pswrd = ""
class Yemek:

    def __init__(self, usrnm, pswrd):

        self.browser = webdriver.Chrome("chromedriver.exe")
        self.usrnm = usrnm
        self.pswrd = pswrd

    def yemekLogin(self):

        self.browser.get("https://www.yemeksepeti.com/kktc")
#       self.browser.maximize_window()

        try:
            usrnmInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='UserName']")));
            pswrdInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='password']")));

            usrnmInput.send_keys(self.usrnm)
            pswrdInput.send_keys(self.pswrd)

            lgnBtn = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ys-fastlogin-button']")));
            lgnBtn.click()
            
            
        except:
            print("Hata")
        time.sleep(2) #bu satırı kaldırınca hata alıyorum..

        
        try:
            ctySlct =WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/span/span[1]/span/span[2]")));
            ctySlct.click()
        except:
            print("Şehir seçme hatası")


        try: 
            Slcttown = self.browser.find_element_by_xpath("//*[@id='ys-areaSelector-droparea']/span/span/span[1]/input")
            Slcttown.send_keys(Keys.ENTER)
        except:
            print("Şehir yok!")


        try:

            srchBtn = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[4]/input")));
            srchBtn.click()
            srchBtn.send_keys("pizza")
            srchBtn.send_keys(Keys.ENTER)
        except:

            print("Arama yapma hatası ")
        

        try:

            frstFood = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/a/i")));
            frstFood.click()

        except:
            print("Çıkan ilk yemeği seçme hatası!")

      

            #foodFrst = self.browser.find_element_by_xpath("//*[@id='cboxLoadedContent']/div/div[2]/div/div[2]/button")
            #foodFrst.click()
            #eğer yemek seçildiğinde bir menü ekranı çıkarsa bu kısmı aktiif etmeliyiz

        try:
            confrmOrder = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='basket-container']/div[2]/div/div[5]/button")));
            confrmOrder.click()

        except:
            print("Sepeti onaylama hatası!")

        
        try:
            payMent = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[8]/div/div/div/div/div[2]/div/div[2]/label/input")));
            payMent.click()
                

        except:
            print("Ödeme yöntemi seçilemedi!")


ymksprs = Yemek(usrnm,pswrd)
ymksprs.yemekLogin()
