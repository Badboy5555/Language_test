from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math, time

class BasePage():
    def __init__(self, driver, url, timeout=10):
        self.browser = driver
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def elements_present(self, how, what):
        elements_text = []
        try:
            elements = self.browser.find_elements(how, what)
            for _ in elements:
                elements_text.append(_.text)
        except (NoSuchElementException):
            return elements_text
        return elements_text


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        #time.sleep(2)
        alert.accept()
        # try:
        #     time.sleep(15)
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")