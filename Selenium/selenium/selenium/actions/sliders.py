"""
baseUrl = "https://jqueryui.com/slider/"
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(element, 100, 0).perform()
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from utilities.takescreenshot import takeScreenShot
class sliders():
    def testSlider(self):
        global childHandle
        baseUrl = "https://jqueryui.com/slider/"
        tss = takeScreenShot()
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        # switch to Iframe
        driver.switch_to.frame(0)
        #slider element
        sliderElement = driver.find_element_by_xpath("//div[@id='slider']//span")
        #slider
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(sliderElement,50,0).perform()
        except:
            print("Slider is false!")
        time.sleep(2)
        # screen shots
        destinationFilename = "C:\\workspace_python\\selenium\\actions\\"
        tss.takeScreenshot(driver, destinationFilename)
        driver.quit()
ff = sliders()
ff.testSlider()