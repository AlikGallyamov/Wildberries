import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def browser_settings():
    options = Options()
    browser.config.window_width = 1600
    browser.config.window_height = 960
    browser.config.base_url = 'https://www.wildberries.ru'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'normal'

    yield

    browser.quit()
