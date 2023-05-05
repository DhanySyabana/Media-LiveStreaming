from seleniumwire import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Selenium:

    def __init__(self, url:str=None, settings:dict={
        "headless": True,
    }, selenium_host:str=None, selenium_port:int=None) -> None:
        self.url = url
        self.driver = None
        self.desired_capabilities = None
        self.options = None
        self.settings = settings
        self.selenium_host = selenium_host
        self.selenium_port = selenium_port
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
        driver = webdriver.Remote(
            command_executor=F"http://{self.selenium_host}:{self.selenium_port}/wd/hub",
            desired_capabilities=self.desired_capabilities,
            options=self.options,
            seleniumwire_options={
                'auto_config': True,
                'host': self.selenium_host,
            }
        )
        self.driver = driver
        return self.driver
    
    def CloseDriver(self) -> None:
        self.driver.quit()
        return None
