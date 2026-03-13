import pytest
from selenium import webdriver
#import time #added this if want to ensure if UI is in propper language

from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb", help="choose lang: 'en-gb', 'ru', 'pl', 'es'")

@pytest.fixture
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    browser.maximize_window()
    yield browser
    #time.sleep(3) #added this if want to ensure if UI is in propper language
    browser.quit()
