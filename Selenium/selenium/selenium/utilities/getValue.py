from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.findElements import findElements
import time
class getValue():
    def test(self):
        baseURL="http://formy-project.herokuapp.com/form"
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #maximize windows
        driver.maximize_window()
        #open URL
        driver.get(baseURL)
        driver.implicitly_wait(5)
        find = findElements(driver)
        #get value
        elementResult = find.isElementPresent("first-name",By.ID)
        print(str(elementResult))
        element = find.getElement("first-name")
        #driver.find_element_by_id("first-name")
        result = element.get_attribute("placeholder")
        print(result)
        resultId = element.get_attribute("id")
        print(resultId)
        #quit driver
        time.sleep(5)
        driver.quit()

ch = getValue()
ch.test()