import pytest
from selenium import webdriver
from urls import Urls
from pages.home_page import HomePage


#@pytest.fixture(scope="session")
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    home_page = HomePage(driver)
    home_page.load(Urls.home_page)

    yield driver

    driver.quit()
