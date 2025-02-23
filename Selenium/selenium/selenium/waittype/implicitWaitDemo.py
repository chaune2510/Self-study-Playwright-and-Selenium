from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.findElements import findElements
import time
class implicitwaitdemo():
    def test(self):
        baseURL="https://www.vietnamairlines.com/us/en/plan-book/flight-package"
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #maximize windows
        driver.maximize_window()
        #open URL
        driver.get(baseURL)
        driver.implicitly_wait(10)
        find = findElements(driver)
        #get value
        elementResult = find.isElementPresent("header_1_rptTabName_ctl02_hplnavTab",By.ID)
        print(str(elementResult))
        element = find.getElement("header_1_rptTabName_ctl02_hplnavTab")
        #driver.find_element_by_id("first-name")
        result = element.get_attribute("data-content-type")
        print(result)
        resultId = element.get_attribute("id")
        print(resultId)
        #quit driver
        time.sleep(5)
        driver.quit()

ch = implicitwaitdemo()
ch.test()