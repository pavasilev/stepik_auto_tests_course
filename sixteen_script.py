import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:
   browser = webdriver.Chrome()
   link = "https://suninjuly.github.io/alert_accept.html"
   browser.get(link)       
 
   button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
   button.click()

   confirm = browser.switch_to.alert
   confirm.accept()
   
   x = browser.find_element(By.ID,"input_value").text
   y = calc(x)
   
   answer = browser.find_element(By.ID,"answer")
   answer.send_keys(y)

   button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
   button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()