# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# # Tạo đối tượng Service với đường dẫn chromedriver
# service = Service("C:\\Users\\minhchou\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.14\\chromedriver.exe")

# # Khởi tạo WebDriver với Service
# driver = webdriver.Chrome(service=service)
# driver.get("https://material.playwrightvn.com/01-xpath-register-page.html")
# input("Nhấn Enter để đóng trình duyệt...")
# driver.quit()

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
        driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
        driver.maximize_window();
        #driver.implicitly_wait(10)
        #Register
        #input username
        driver.find_element(By.NAME, "Email or username").send_keys("test02")
        #input password
        driver.find_element(By.NAME, "Password").send_keys("test02")
        # time.sleep(5000)
        #quit driver
        # driver.quit()
ch = Test()
ch.testChrome()