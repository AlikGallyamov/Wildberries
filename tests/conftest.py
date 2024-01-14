import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from wildberries_tests.controls import attach
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def browser_settings():
    options = Options()
    browser.config.window_width = 1600
    browser.config.window_height = 960
    browser.config.base_url = 'https://www.wildberries.ru'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'normal'
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.driver_options = driver_options

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
