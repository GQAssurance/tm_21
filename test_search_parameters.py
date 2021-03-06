from selenium import webdriver
import pytest
import os


@pytest.fixture(scope='session')
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def base_url():
    if "BASE_URL" in os.environ.keys():
        return os.environ["BASE_URL"]
    else:
        return "https://www.google.com"


@pytest.fixture(scope='function')
def search_terms():
    if "SEARCH_TERMS" in os.environ.keys():
        return os.environ["SEARCH_TERMS"].split(",")
    else:
        return ["default"]


@pytest.mark.parameterized
def test_search(web_driver, base_url, search_terms):
    print("\n")
    for term in search_terms:
        web_driver.get(base_url + "/search?q=" + term)
        print(web_driver.title)
        assert term in web_driver.title
