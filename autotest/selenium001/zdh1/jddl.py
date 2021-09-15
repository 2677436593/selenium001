from Day_05.basepage import BasePage
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class ymfz(BasePage):
    bd_loc1 = (By.CLASS_NAME,"link-login")
    bd_loc2 = (By.CLASS_NAME,"QQ-icon")
    bd_loc3 = (By.ID, "ptlogin_iframe")
    bd_loc4 = (By.LINK_TEXT, "帐号密码登录")
    bd_loc5 = (By.NAME, "u")
    bd_loc6 = (By.NAME, "p")
    bd_loc7 = (By.ID,"login_button")
    def kw(self):
        self.driver = webdriver.Firefox()
        self.dkwz('https://www.jd.com')

    def dl(self):
        self.dj(*self.bd_loc1)      #点击请登录

    def qq(self):
        self.dj(*self.bd_loc2)      #点击qq

    def iframe(self):
        f = self.dingwei(*self.bd_loc3)     #iframe框架
        self.driver.switch_to.frame(f)

    def dlfs(self):
        self.dj(*self.bd_loc4)      #帐号密码登录

    def zhanghao(self):
        self.sr(*self.bd_loc5,"2677436593")     #账号输入

    def mima(self):
        self.sr(*self.bd_loc6,"xll322322")      #密码输入

    def sqdl(self):
        self.dj(*self.bd_loc7)      #点击授权登录

    def jddl(self):
        self.kw()
        sleep(2)
        self.dl()
        sleep(2)
        self.qq()
        sleep(2)
        self.iframe()
        sleep(2)
        self.dlfs()
        sleep(2)
        self.zhanghao()
        sleep(2)
        self.mima()
        sleep(2)
        self.sqdl()




