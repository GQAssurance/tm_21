from selenium import webdriver
import os
import pytest


@pytest.fixture(scope='session')
def web_driver():
    options = webdriver.ChromeOptions()
    if "DISPLAY" in os.environ.keys():
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
    else:
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()


@pytest.mark.search_test_v3
def test_search(web_driver):
    search_term = "qa"
    web_driver.get("https://www.google.com/search?q=" + search_term)
    assert search_term in web_driver.title
