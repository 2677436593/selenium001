import unittest
from Day_05.jddl import ymfz
from selenium import webdriver
from time import sleep
from Day_05.jdyd import jdyd

class baidu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Edge(r"C:\Users\ASUS\PycharmProjects\cs1903A\Day_01\IEDriverServer.exe")
        sleep(2)
    def tearDown(self) -> None:
        self.driver.quit()
    def test_dl(self):
        po=ymfz(self.driver)
        po.jddl()
        sleep(2)
    def test_jdyd(self):
        po=jdyd(self.driver)
        po.jdyd()
        sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)