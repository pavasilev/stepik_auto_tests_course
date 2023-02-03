from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID,"num1").text
    num_2 = browser.find_element(By.ID,"num2").text
    sum = str((int(num_1) + int(num_2)))
    
    select = Select(browser.find_element(By.CLASS_NAME,"custom-select"))
    select.select_by_value(sum)
    
    button_1 = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    button_1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
