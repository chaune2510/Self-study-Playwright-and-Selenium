"""
Xpath:
//tagname[attribute]
CSS Selector:
# -> id
.-> class
"""
from selenium import webdriver
import os

class findElementByXpathCss():
    def testMethod(self):
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        # open the browers
        driver.get("https://the-internet.herokuapp.com/login")
        # use xpath
        driver.find_element_by_xpath("//input[@id='username']").clear()
        driver.find_element_by_xpath("//input[@id='username']").send_keys("tomsmith")

        # use Css
        driver.find_element_by_css_selector("#password").clear()
        driver.find_element_by_css_selector("#password").send_keys("SuperSecretPassword!")
        # button
        driver.find_element_by_xpath("//button[@type='submit']").click()

xpathcss = findElementByXpathCss()
xpathcss.testMethod()