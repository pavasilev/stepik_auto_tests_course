import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:
   browser = webdriver.Chrome()
   browser.implicitly_wait(5)
   browser.get("https://suninjuly.github.io/explicit_wait2.html")

   button = browser.find_element(By.ID,"book")
   price = WebDriverWait(browser, 12).until(
          EC.text_to_be_present_in_element((By.ID,"price"), "100")
       )
   button.click()

   x = browser.find_element(By.ID,"input_value").text
   y = calc(x)
   answer = browser.find_element(By.ID,"answer")
   answer.send_keys(y)
   browser.find_element(By.ID,"solve").click()

finally:
       time.sleep(10)
       browser.quit()







