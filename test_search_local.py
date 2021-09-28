from selenium import webdriver
import pytest


@pytest.mark.search_local
def google_search(search_term):
    # Use a breakpoint in the code line below to debug your script.
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/search?q=" + search_term)
    print(driver.title)
    assert search_term in driver.title
    driver.close()


def test_search():
    google_search('qa')
