from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

WEBSITE_URL =
WEBDRIVER_PATH =

class RandomMovieTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument('--headless') # If you want a headless webdriver
        self.driver = webdriver.Firefox(
            executable_path=WEBDRIVER_PATH, options=options)

    def tearDown(self):
        self.driver.quit()

    def test_website_title(self):
        self.driver.get(WEBSITE_URL)
        self.assertIn('Random Website', self.driver.title)


unittest.main()
