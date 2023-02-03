import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    form_1 = browser.find_element(By.ID,"answer")
    form_1.send_keys(y)    

    check_1 = browser.find_element(By.ID,"robotCheckbox")
    check_1.click()

    radio_1 = browser.find_element(By.ID,"robotsRule")
    radio_1.click()

    button_1 = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    button_1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
