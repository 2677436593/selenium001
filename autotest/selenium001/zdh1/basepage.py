from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class BasePage():
    def __init__(self,driver):
        self.driver=driver
    def dkwz(self,url):     #打开网址
        self.driver.get(url)
    def dingwei(self,*loc):     #定位
        return self.driver.find_element(*loc)
    def xsdd(self,sj1,sj2):     #显示等待
        return WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((sj1, sj2)))
    def ysdd(self):
        self.driver.implicitly_wait(5)     #隐示等待
    def ckqh(self):     #切换窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
    def sx(self):       #刷新
        self.driver.refresh()
    def sbdj(self,cz):      #鼠标点击
        ActionChains(self.driver).click(cz).perform()
    def hddb1(self):       #滚动到顶部
        self.driver.execute_script('window.scrollTo(0,0)')
    def hd(self,x):
        self.driver.execute_script(x)
    def hddb(self):     #滚动到底部
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    def sbxt(self,cz):     #鼠标悬停
        ActionChains(self.driver).move_to_element(cz).perform()
    def sr(self,fs,loc,sj):       #输入
        return self.driver.find_element(fs,loc).send_keys(sj)
    def dj(self,*loc):      #点击
        return self.driver.find_element(*loc).click()

