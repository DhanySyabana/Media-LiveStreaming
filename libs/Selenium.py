from seleniumwire import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

class Selenium:

    def __init__(self, url:str=None, settings:dict={
        "headless": True,
    }) -> None:
        self.url = url
        self.driver = None
        self.desired_capabilities = None
        self.options = None
        self.settings = settings
        super().__init__()

    def SeleniumCapabilities(self) -> DesiredCapabilities:
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        self.desired_capabilities = desired_capabilities
        return self.desired_capabilities

    def SeleniumOptions(self) -> webdriver.ChromeOptions:
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")

        if self.settings["headless"]:
            options.add_argument("--headless")

        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("start-maximized")
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--mute-audio")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument(f'user-agent={self.desired_capabilities}')
        self.options = options
        return self.options

    def DriverSelenium(self) -> webdriver.Chrome:
        driver = webdriver.Chrome(
            options=self.options,
            # desired_capabilities=self.desired_capabilities
        )
        self.driver = driver
        return self.driver
    
    def CloseDriver(self) -> None:
        self.driver.quit()
        return None
