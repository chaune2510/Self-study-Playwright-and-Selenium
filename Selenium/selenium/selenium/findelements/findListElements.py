"""

    find_elements_by_name
    find_elements_by_xpath
    find_elements_by_link_text
    find_elements_by_partial_link_text
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector

"""
from selenium import webdriver
import os

class findElements():
    def testMethod(self):
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        # open the browers
        driver.get("http://formy-project.herokuapp.com/form")
        #find elements
        listElements = driver.find_elements_by_class_name("form-control")
        length = len(listElements)
        i=0
        for element in listElements:
            if i<3:
                element.send_keys("aaaaaa")
                i=i+1

lstElements = findElements()
lstElements.testMethod()