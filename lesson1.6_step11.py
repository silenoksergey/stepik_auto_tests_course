from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()

##Ссылка без бага http://suninjuly.github.io/registration1.html
##Ссылка с багом http://suninjuly.github.io/registration2.html

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    required_field1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    required_field1.send_keys("Sergey")

    required_field2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    required_field2.send_keys("Silenok")

    required_field3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    required_field3.send_keys("Silenok@gmail.com")

   # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()