"""
actions = ActionChains(driver)
actions.drag_and_drop(fromElement, toElement).perform()
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from utilities.takescreenshot import takeScreenShot
class drapanddrop():
    def testDrapAndDrop(self):
        global childHandle
        baseUrl = "https://jqueryui.com/droppable/"
        tss = takeScreenShot()
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        # switch to Iframe
        driver.switch_to.frame(0)
        #from element
        fromElement = driver.find_element_by_id("draggable")
        #to element
        toElement = driver.find_element_by_id("droppable")
        #drap and drop
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(fromElement,toElement).perform()
        except:
            print("Drap and drop is false!")
        time.sleep(4)
        # screen shots
        destinationFilename = "C:\\workspace_python\\selenium\\actions\\"
        tss.takeScreenshot(driver, destinationFilename)
        driver.quit()
ff = drapanddrop()
ff.testDrapAndDrop()