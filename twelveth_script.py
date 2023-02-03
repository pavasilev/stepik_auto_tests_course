import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_element = browser.find_element(By.CSS_SELECTOR,"img#treasure")
    treasure_attribute = treasure_element.get_attribute("valuex")
    x = treasure_attribute
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
