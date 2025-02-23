import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test():
    def testChrome(self):
        #initiate driver
        #driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        driver = webdriver.Chrome()

        #open url
        driver.get("http://localhost/register/register.php")
        driver.maximize_window();
        driver.implicitly_wait(10)
        #Register
        #input username
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("test02")
        #input email
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("test02@gmail.com")
        #input password
        driver.find_element_by_name("password_1").clear()
        driver.find_element_by_name("password_1").send_keys("test02")
        #input conform password
        driver.find_element_by_name("password_2").clear()
        driver.find_element_by_name("password_2").send_keys("test02")
        #click on register button
        driver.find_element_by_name("reg_user").click()
        #verify register success
        userLogout = driver.find_element(By.XPATH, "//a[contains(text(),'logout')]")
        if userLogout is not None:
            print("Register Successful")
        else:
            print("Register Failed")
        #click logout
        driver.find_element_by_xpath("//a[contains(text(),'logout')]").click()
        time.sleep(5)
        #Login page
        #input username
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("test02")
        #input password
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("test02")
        #click onn login button
        driver.find_element_by_name("login_user").click()
        #verify login success
        if userLogout is not None:
            print("Login Successful")
        else:
            print("Login Failed")
        time.sleep(5)
        #quit driver
        driver.quit()
ch = Test()
ch.testChrome()