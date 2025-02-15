from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://agrichain.com/qa/input"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_input(self, text):
        input_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter String Input...']")
        input_field.clear()
        input_field.send_keys(text)

    def click_submit(self):
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
