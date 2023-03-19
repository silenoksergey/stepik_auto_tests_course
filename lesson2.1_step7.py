import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    treasure_img = browser.find_element(By.ID, "treasure")
    find_x = treasure_img.get_attribute("valuex")
    result_x = calc(find_x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result_x)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()

    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button1.click()


finally:
    time.sleep(5)
    browser.quit()
