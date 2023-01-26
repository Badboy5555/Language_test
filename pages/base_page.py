class BasePage():
    def __init__(self, driver, url):
        self.browser = driver
        self.url = url

    def open(self):
        self.browser.get(self.url)