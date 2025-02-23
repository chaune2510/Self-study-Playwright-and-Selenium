"""
Switch to the window using its title
driver.switch_to.window("window_title")
Get current window handle
current_window_handle = driver.current_window_handle
Get all window handles
window_handles = driver.window_handles
Switch to the second window handle
#Get all window handles
window_handles = driver.window_handles
#List start with the 0 index
driver.switch_to.window(window_handles[1])
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.takescreenshot import takeScreenShot
class SwitchToWindow():

    def test(self):
        global childHandle
        baseUrl = "http://formy-project.herokuapp.com/switch-window"
        tss = takeScreenShot()
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)


        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent handle: " + str(parentHandle))

        # Find open window button and click it
        driver.find_element_by_id("new-tab-button").click()
        time.sleep(5)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles
        for handle in handles:
            if handle != parentHandle:
                childHandle = handle
                print("Handle: " + str(handles))
        driver.switch_to.window(childHandle)
        driver.find_element_by_link_text("Autocomplete").click()
        time.sleep(5)

        # screen shots
        destinationFilename = "C:\\workspace_python\\selenium\\switchto\\"
        tss.takeScreenshot(driver, destinationFilename)

ff = SwitchToWindow()
ff.test()