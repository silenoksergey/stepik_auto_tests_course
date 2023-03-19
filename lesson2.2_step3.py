import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/selects2.html")
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    result_sum = num1 + num2

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(result_sum))

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

finally:
    time.sleep(5)
    browser.quit()
