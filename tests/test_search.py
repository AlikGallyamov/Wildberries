from wildberries_tests.data.data_cards import card
from wildberries_tests.pages.main_page import MainPage


def test_search_by_name():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.result_by_name(card.card_name)


def test_search_by_article():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_article)
    main_page.result_by_article(card.card_article)
