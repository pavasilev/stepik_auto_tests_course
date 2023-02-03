import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/execute_script.html"
	browser.get(link)

	x = browser.find_element(By.ID,"input_value")
	y = calc(x.text)

	browser.execute_script("window.scrollBy(0, 100);")

	answer_form = browser.find_element(By.ID,"answer")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", answer_form)
	answer_form.send_keys(y)

	browser.find_element(By.ID,"robotCheckbox").click()
	browser.find_element(By.ID,"robotsRule").click()

	button_1 = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
	button_1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()