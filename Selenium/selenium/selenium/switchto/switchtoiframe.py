"""
 # Switch to frame using Id
 driver.switch_to.frame("")

 # Switch to frame using name
driver.switch_to.frame("iframe-name")

  # Switch to frame using numbers
  driver.switch_to.frame(0)
  driver.switch_to_default_content()
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.takescreenshot import takeScreenShot
class SwitchToIframe():

    def test(self):
        baseUrl = "https://jqueryui.com/draggable/"
        tss = takeScreenShot()
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Find iframe handle -> Main Window
        list_Iframe = driver.find_element_by_tag_name("iframe")
        print(list_Iframe)

        # switch to Iframe
        driver.switch_to.frame(0)

        # Find all handles, there should two handles after get text one lement
        strDragMe = driver.find_element_by_xpath("//p[contains(text(),'Drag me around')]").text
        if strDragMe == "Drag me around":
            print(True)
        else:
            print(False)
        driver.switch_to_default_content()
        strH1 = driver.find_element_by_xpath("//h1[@class='entry-title']").text
        if strH1 == "Draggable":
            print(True)
        else:
            print(False)
        # screen shots
        destinationFilename = "C:\\workspace_python\\selenium\\switchto\\"
        tss.takeScreenshot(driver, destinationFilename)
        time.sleep(5)
        driver.quit()
ff = SwitchToIframe()
ff.test()