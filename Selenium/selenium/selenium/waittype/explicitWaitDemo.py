from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.findElements import findElements
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class explicitwaitdemo():
    def test(self):
        baseURL="https://www.expedia.com/"
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #maximize windows
        driver.maximize_window()
        #open URL
        driver.get(baseURL)
        driver.implicitly_wait(10)
        find = findElements(driver)
        #explicit wait
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable(By.ID,"tab-flight-tab-hp"))
        element.click()
        #quit driver
        time.sleep(5)
        driver.quit()

ch = explicitwaitdemo()
ch.test()