from selenium import webdriver
import time
class elementState():
    def test(self):
        baseURL="https://www.google.com/"
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #maximize windows
        driver.maximize_window()
        #open URL
        driver.get(baseURL)
        #click link form
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("selenium")
        time.sleep(5)

        driver.quit()
        
ch = elementState()
ch.test()