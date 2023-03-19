from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/find_xpath_form")
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Sergey")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Silenok")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Magnirogorsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла