"""
link Text
partial Link Text
"""
from selenium import webdriver
import os

class findElementByLinkText():
    def testMethod(self):
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        # open the browers
        driver.get("https://the-internet.herokuapp.com/")
        #click login
        #driver.find_element_by_link_text("Form Authentication").click()
        driver.find_element_by_partial_link_text("Form").click()
        # use xpath
        driver.find_element_by_xpath("//input[@id='username']").clear()
        driver.find_element_by_xpath("//input[@id='username']").send_keys("tomsmith")

        # use Css
        driver.find_element_by_css_selector("#password").clear()
        driver.find_element_by_css_selector("#password").send_keys("SuperSecretPassword!")
        # button
        driver.find_element_by_xpath("//button[@type='submit']").click()

linkText = findElementByLinkText()
linkText.testMethod()