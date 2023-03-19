
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
browser.implicitly_wait(5)

try:

    verify_button = browser.find_element(By.ID, "verify")
    verify_button.click()
    verify_message = browser.find_element(By.ID, "verify_message")

    assert "successful" in verify_message.text


finally:

    browser.quit()
