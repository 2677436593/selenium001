from Day_05.basepage import BasePage
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
class jdyd(BasePage):
    jd_loc1 = (By.XPATH, '/html/body/div[1]/div[5]/div[1]/div[3]/div[3]/div[1]/ul/li[3]/a/span[2]')
    jd_loc2 = (By.ID, 'searchBtn')
    jd_loc3 = (By.CLASS_NAME, 'err-product')
    def kw(self):
        self.driver = webdriver.Firefox()
        self.dkwz('https://www.jd.com')

    def ss(self):
        self.dj(*self.jd_loc1)

    def hck(self):
        self.ckqh()

    def dj1(self):
        self.dj(*self.jd_loc2)

    def hdck(self):
        self.hd('window.scrollTo(0,500)')

    def jdyd1(self):
        self.dj(*self.jd_loc3)


    def jdyd(self):
        self.kw()
        sleep(2)
        self.ss()
        sleep(2)
        self.hck()
        sleep(2)
        self.dj1()
        sleep(2)
        self.hdck()
        sleep(2)
        self.jdyd1()
        sleep(2)

