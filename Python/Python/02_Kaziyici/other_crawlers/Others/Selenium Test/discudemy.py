from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Udemy:
	def __init__(self):

		self.browser = 	webdriver.Chrome("chromedriver.exe")

	def trLang(self):
		self.browser.get("https://www.discudemy.com/")
#		self.browser.maximize_window()
		try:
			clckWrld = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/nav[1]/a[4]/i")));
			clckWrld.click()

		except:
			print("hata")

		try:
			slctTr = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/section/div[47]")));
			slctTr.click()
		except:
			print("hata!")
courses = Udemy()
courses.trLang()