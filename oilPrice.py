from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup as bs
import telepot

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
driver.get("http://www.opinet.co.kr/user/main/mainView.do")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ML10 > .text-3")))

today = driver.find_elements(By.CSS_SELECTOR, ".today > .text-2")
oil_price = driver.find_elements(By.CSS_SELECTOR, ".ML10 > .text-3")

print("{0} 전국평균: {1}".format(today[0].text, oil_price[0].text))

token = "token"
bot = telepot.Bot(token)

userList = ['a', 'b']

for user in userList:
    bot.sendMessage(user, "{0} 전국평균: {1}".format(today[0].text, oil_price[0].text))

driver.quit()
