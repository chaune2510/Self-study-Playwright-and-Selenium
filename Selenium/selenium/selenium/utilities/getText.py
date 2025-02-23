from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class getText():
    def test(self):
        baseURL="http://formy-project.herokuapp.com/form"
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #maximize windows
        driver.maximize_window()
        #open URL
        driver.get(baseURL)
        driver.implicitly_wait(5)
        #get Text
        h1 = driver.find_element_by_xpath("//h1")
        strH1 = h1.text
        print(strH1)
        #quit driver
        time.sleep(5)
        driver.quit()

ch = getText()
ch.test()