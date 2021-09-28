from selenium import webdriver
import pytest

@pytest.mark.search_docker
def google_search(search_term):
    # Use a breakpoint in the code line below to debug your script.
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/search?q=" + search_term)
    print(driver.title)
    assert search_term in driver.title
    driver.close()



def test_search():
    google_search('qa')
