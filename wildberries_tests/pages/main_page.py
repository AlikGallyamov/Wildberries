from selene import browser, be, have

import time


class MainPage:
    def __init__(self):
        self.search_input = browser.element('#searchInput')

    def open_url(self):
        browser.open('/')
        time.sleep(3)

    def search(self, value):
        self.search_input.type(value).press_enter()

    def result_by_name(self, card_name):
        browser.element('[data-nm-id="150179366"] a').should(have.attribute('aria-label', card_name))

    def result_by_article(self, card_article):
        browser.element('#productNmId').should(have.text(card_article))
