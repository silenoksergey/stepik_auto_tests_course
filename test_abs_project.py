from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class Test_input(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def fill_form(self, link):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Sergey")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Silenok")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("Silenok@gmail.com")
        browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

        finnaly_text = browser.find_element(By.TAG_NAME, "h1").text
        return finnaly_text

    def test_result_text_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fill_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_result_text_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = self.fill_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
