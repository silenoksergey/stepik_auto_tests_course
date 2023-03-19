import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/math.html")
    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    result_x = calc(x)
    input1 = browser.find_element(By.CLASS_NAME, "form-control")
    input1.send_keys(result_x)
    checkbox1 = browser.find_element(By.CSS_SELECTOR, ".form-check-input[id='robotCheckbox']")
    checkbox1.click()
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button1.click()


finally:
    time.sleep(5)
    browser.quit()
