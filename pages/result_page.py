from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def get_output(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'Output is:')]/following-sibling::div").text

    def click_back_to_home(self):
        self.driver.find_element(By.XPATH, "//button[text()='Back to Home']").click()
