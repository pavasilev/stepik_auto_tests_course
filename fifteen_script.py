import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
   browser = webdriver.Chrome()
   link = "https://suninjuly.github.io/file_input.html"
   browser.get(link)
   fields = browser.find_elements(By.CLASS_NAME,"form-control")
   for element in fields:
       element.send_keys("test")
        
        
   current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
   file_path = os.path.join(current_dir, 'new.txt')           # добавляем к этому пути имя файла 
   button = browser.find_element(By.CSS_SELECTOR,"[type='file']")
   button.send_keys(file_path)

   button_1 = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
   button_1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()