from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_appears(browser):
    browser.get(link)

    add_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket'))
    ) 
    
    assert add_button is not None, "Can't see the 'Add to Basket', sorry!"

    # print ('OK: PASSED')
    

