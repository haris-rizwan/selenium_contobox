import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginClass

@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method  level teardown")

# test module is a a test.py file
@pytest.fixture(scope="class")
def OnetimesetUp(request,browser,baseurl):
    wdf = WebDriverFactory(browser)
    driver=wdf.getWebDriverInstance()
    # lp = LoginClass(driver)
    # lp.Login("test@email.com","abcabc")
    print("*"* 20 + "One time modular set up " + "*"* 20)
    if request.cls is not None:
        # if the class value is not none then return the value from one time setup to
        # to the test class
          request.cls.driver = driver
    yield driver
    # driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--OStype")
    parser.addoption("--baseurl")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def baseurl(request):
    return request.config.getoption("--baseurl")