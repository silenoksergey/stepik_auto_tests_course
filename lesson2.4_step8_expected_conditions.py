from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    button = browser.find_element(By.ID, "book")

    wait_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button.click()
    find_x = browser.find_element(By.ID, "input_value").text

    find_input = browser.find_element(By.ID, "answer")
    find_input.send_keys(calc(find_x))

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()


