import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")


try:
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    allert = browser.switch_to.alert
    allert.accept()
    find_x = browser.find_element(By.ID, "input_value").text
    result_x = calc(find_x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result_x)

    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
