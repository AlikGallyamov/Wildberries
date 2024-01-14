from selene import browser, be, have, query, command
from wildberries_tests.data.data_cards import Texts

import time


class MainPage:
    def __init__(self):
        self.search_input = browser.element('#searchInput')
        self.basket = browser.element('[class*=item-basket]')

    def open_url(self):
        browser.open('/')
        browser.element('[class="general-preloader"]').should(be.not_.visible)


    def search(self, value):
        self.search_input.type(value).press_enter()

    def result_by_name(self, card_name, brand_name, card_article):
        browser.element(f'[data-nm-id="{card_article}"] a').should(have.attribute('aria-label', f'{card_name} {brand_name}'))

    def result_by_article(self, card_article):
        browser.element('#productNmId').should(have.text(card_article))

    def no_result(self):
        browser.element('.not-found-search__text').should(have.text(Texts.nothing_found))

    def add_item_to_cart(self, card_article):

        browser.element(f'[data-nm-id="{card_article}"]').hover()
        browser.element(f'[data-nm-id="{card_article}"] [class*="card__add"]').click()

    def open_basket(self):
        self.basket.click()
    def check_cart(self, card_name, brand_name):
        self.open_basket()
        browser.all('[class="good-info__title j-product-popup"] span').should(have.texts(card_name, brand_name))

    def remove_from_cart(self):
        self.open_basket()
        browser.element('[class*=item-del]').click()
        browser.element('[class*="basket-empty__title"]').should(have.text(Texts.empty_cart))



