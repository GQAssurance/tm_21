from selenium import webdriver
import pytest


@pytest.fixture(scope='session')
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.mark.local
def test_search(web_driver):
    search_term = "desktop"
    web_driver.get("https://www.google.com/search?q=" + search_term)
    print("\n"+web_driver.title)
    assert search_term in web_driver.title


