'''
Про UNITTEST:
1. Каждый тест — это метод, который начинается с test_   (e.g def test_something(self):)
2. Тесты находятся внутри класса, который наследует unittest.TestCase (e.g class Name_of_your_test (unittest.TestCase):)
*3. setUp() запускается перед КАЖДЫМ тестом. Каждый тест получает новый, чистый браузер.
*4. tearDown() запускается после КАЖДОГО теста. Это гарантирует, что тесты не мешают друг другу.
    *!!! 3 и 4 функции всегда пишутся ВНУТРИ класса и ПЕРЕД тестами, но это не потому что «так надо по порядку», а потому что unittest сам вызывает их в нужный момент.
5. Тесты НЕ зависят друг от друга. каждый тест — отдельный запуск браузера. Последующий тест не знает что сделал предыдущий тест
6. Проверки делаются через assert‑методы  (самый популярный - self.assertEqual(actual, expected) Если не совпало — тест падает.
7. Запуск тестов — через стандартный блок
if __name__ == "__main__":
 unittest.main()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest 


class Complete_registration(unittest.TestCase):
    # Step 1 ПЕРЕД тестом обязательно вставляем блок def setUp(self) - чтобы открыть браузер
    '''
    setUp() — запускается перед КАЖДЫМ тестом. Каждый тест получает свой собственный браузер.
    - создаёт браузер
    - настраивает окружение
    - готовит всё, что нужно тесту'''
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
    
    # Step 2 ПЕРЕД тестом обязательно вставляем блок def tearDown(self)  - чтобы закрыть браузер
    '''
    tearDown() — запускается после КАЖДОГО теста
    закрывает браузер
    очищает ресурсы
    завершает всё, что тест открыл'''
    def tearDown(self):
        self.browser.quit()
    
    # Step 3 - тут наш тест скрипт   
    '''
    надо засовывать все в одну функцию(один тест) тк unittest запускает каждый тест в отдельном браузере. ЗАПОМНИ:
      каждый тест(def) должен быть изолирован
      каждый тест(def) должен работать сам по себе
      нельзя рассчитывать, что «предыдущий тест(def) что‑то сделал» '''
    def test_fill_in_form1(self): 
        self.browser.get("http://suninjuly.github.io/registration1.html") #exspected result: test passed
        #self.browser.get("http://suninjuly.github.io/registration2.html")

        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys('Jadviga')
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys('Kowalska')
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys('a.ren@text.com')  
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        ).click()
    
        expected_welcome_text = "Congratulations! You have successfully registered!" #
        actual_welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(actual_welcome_text, expected_welcome_text, \
        f"Expected {expected_welcome_text}, but got {actual_welcome_text}")
        #print("OK: text matches")
#и это в конце
if __name__ == "__main__":
    unittest.main()


class Complete_registration2(unittest.TestCase):

    # Step 1 ПЕРЕД тестом обязательно вставляем блок def setUp(self) - чтобы открыть браузер
    '''
    setUp() — запускается перед КАЖДЫМ тестом. Каждый тест получает свой собственный браузер.
    - создаёт браузер
    - настраивает окружение
    - готовит всё, что нужно тесту'''
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
    
    # Step 2 ПЕРЕД тестом обязательно вставляем блок def tearDown(self)  - чтобы закрыть браузер
    '''
    tearDown() — запускается после КАЖДОГО теста
    закрывает браузер
    очищает ресурсы
    завершает всё, что тест открыл'''
    def tearDown(self):
        self.browser.quit()
    
    # Step 3 - тут наш тест скрипт   
    '''
    надо засовывать все в одну функцию(один тест) тк unittest запускает каждый тест в отдельном браузере. ЗАПОМНИ:
      каждый тест(def) должен быть изолирован
      каждый тест(def) должен работать сам по себе
      нельзя рассчитывать, что «предыдущий тест(def) что‑то сделал» '''
    def test_fill_in_form1(self): 
        #self.browser.get("http://suninjuly.github.io/registration1.html") #exspected result: test passed
        self.browser.get("http://suninjuly.github.io/registration2.html")

        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys('Jadviga')
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys('Kowalska')
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys('a.ren@text.com')  
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        ).click()
    
        expected_welcome_text = "Congratulations! You have successfully registered!" #
        actual_welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(actual_welcome_text, expected_welcome_text, \
        f"Expected {expected_welcome_text}, but got {actual_welcome_text}")
        #print("OK: text matches")
#и это в конце
if __name__ == "__main__":
    unittest.main()
