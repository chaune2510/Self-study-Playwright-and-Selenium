"""
actions = ActionChains(driver)
actions.move_to_element(element).perform()
actions.move_to_element(topLink).click().perform()
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from utilities.takescreenshot import takeScreenShot
class mouseHover():
    def testHover(self):
        global childHandle
        baseUrl = "http://the-internet.herokuapp.com/hovers"
        tss = takeScreenShot()
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        #image
        image = driver.find_element_by_xpath("//div[@class='example']//div[1]//img[1]")
        #link
        link = driver.find_element_by_xpath("//div[@class='example']//div[1]//div[1]//a[1]")
        #mouse hover
        try:
            actions = ActionChains(driver)
            actions.move_to_element(image).click(link).perform()
        except:
            print("Mouse hover is false!")
        time.sleep(2)
        # screen shots
        destinationFilename = "C:\\workspace_python\\selenium\\actions\\"
        tss.takeScreenshot(driver, destinationFilename)
        driver.quit()
ff = mouseHover()
ff.testHover()