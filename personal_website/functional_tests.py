import os
from selenium import webdriver
from pyvirtualdisplay import Display
import unittest

display = Display(visible=0, size=(800, 600))
display.start()

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.display= Display(visible=0, size=(800, 600))
        self.display.start()
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
        self.display.stop()
    def test_can_open_up_webpage_just_fine(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Jason', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()




