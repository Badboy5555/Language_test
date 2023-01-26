class BasePage():
    def __init__(self, driver, url):
        self.bowser = driver
        self.url = url

    def open(self):
        self.browser.get(self.url)