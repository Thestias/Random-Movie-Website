import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest
import time

WEBSITE_URL = 'http://localhost:8000/'
WEBDRIVER_PATH = 'geckodriver'

USERNAME_TO_CREATE = ''
EMAIL_TO_CREATE = ''
PASSWORD_TO_CREATE = ''


class RandomMovieTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # If you want a headless webdriver
        self.driver = webdriver.Firefox(
            executable_path=WEBDRIVER_PATH, options=options)

    def tearDown(self):
        self.driver.quit()

    def test_website_title(self):
        self.driver.get(WEBSITE_URL)
        self.assertIn('Random Website', self.driver.title)


class UsersTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # If you want a headless webdriver
        self.driver = webdriver.Firefox(
            executable_path=WEBDRIVER_PATH, options=options)

    def tearDown(self):
        self.driver.quit()

    def test_user_creation(self):
        self.driver.get(WEBSITE_URL)
        self.driver.find_element_by_id('register').click()
        time.sleep(2)

        username_input = self.driver.find_element_by_id('id_username')
        username_input.send_keys(USERNAME_TO_CREATE)

        email_input = self.driver.find_element_by_id('id_email')
        email_input.send_keys(EMAIL_TO_CREATE)

        password_input = self.driver.find_element_by_id('id_password1')
        password_input.send_keys(PASSWORD_TO_CREATE)

        password_c_input = self.driver.find_element_by_id('id_password2')
        password_c_input.send_keys(PASSWORD_TO_CREATE)

        time.sleep(3)
        self.driver.find_element_by_id('boton').click()
        time.sleep(3)

        self.assertEqual(WEBSITE_URL + 'login/', self.driver.current_url)


class test_user_login(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # If you want a headless webdriver
        self.driver = webdriver.Firefox(
            executable_path=WEBDRIVER_PATH, options=options)

    def tearDown(self):
        self.driver.quit()

    def test_user_login(self):
        self.driver.get(WEBSITE_URL)
        self.driver.find_element_by_id('login').click()
        time.sleep(3)

        username_i = self.driver.find_element_by_id('id_username')
        username_i.send_keys(USERNAME_TO_CREATE)

        password_i = self.driver.find_element_by_id('id_password')
        password_i.send_keys(PASSWORD_TO_CREATE)

        self.driver.find_element_by_id('boton').click()
        time.sleep(2)

        self.assertEqual(WEBSITE_URL, self.driver.current_url)


unittest.main()
