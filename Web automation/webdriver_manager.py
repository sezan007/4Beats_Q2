# webdriver_manager.py

from selenium import webdriver

class WebDriverManager:
    _driver = None

    @staticmethod
    def get_driver():
        """Get the singleton WebDriver instance."""
        if WebDriverManager._driver is None:
            WebDriverManager._driver = webdriver.Chrome()
        return WebDriverManager._driver

    @staticmethod
    def quit_driver():
        """Quit and clean up the WebDriver instance."""
        if WebDriverManager._driver is not None:
            WebDriverManager._driver.quit()
            WebDriverManager._driver = None
