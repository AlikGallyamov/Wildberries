import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pydantic_settings import BaseSettings

from wildberries_tests.controls import attach
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


class Settings(BaseSettings):
    window_width: str = '1600'
    window_height: str = '950'
    base_url: str = 'https://www.wildberries.ru'
    remote: bool = True


@pytest.fixture(autouse=True)
def browser_settings():
    config = Settings()
    options = Options()

    driver_options = webdriver.ChromeOptions()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    if config.remote:
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options)
        browser.config.driver = driver

    browser.config.driver_options = driver_options
    browser.config.base_url = config.base_url
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
