"""
#Switch to alert window
alert = driver.switch_to_alert()
To read the text of Alert window –
#Get Text
strAlertText = alert.text;
accept an Alert (to click on OK/Yes) –
alert.accept()
To dismiss an Alert (to click on Cancel/No) –
alert.dismiss()

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.takescreenshot import takeScreenShot
class SwitchToAlert():

    def test(self):
        global childHandle
        baseUrl = "http://the-internet.herokuapp.com/javascript_alerts"
        tss = takeScreenShot()
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        #click alert
        driver.find_element_by_xpath("//button[contains(text(),'Click for JS Alert')]").click()
        time.sleep(2)
        #switch to alert
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        # screen shots
        destinationFilename = "C:\\workspace_python\\selenium\\switchto\\"
        tss.takeScreenshot(driver, destinationFilename)
    def testConfirm(self):
        global childHandle
        baseUrl = "http://the-internet.herokuapp.com/javascript_alerts"
        tss = takeScreenShot()
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        #click alert
        driver.find_element_by_xpath("	//button[contains(text(),'Click for JS Confirm')]").click()
        time.sleep(2)
        #switch to alert
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(2)
        # screen shots
        destinationFilename = "C:\\workspace_python\\selenium\\switchto\\"
        tss.takeScreenshot(driver, destinationFilename)
        driver.quit()

    def testPromt(self):
        global childHandle
        baseUrl = "http://the-internet.herokuapp.com/javascript_alerts"
        tss = takeScreenShot()
        # initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        # click alert
        driver.find_element_by_xpath("//button[contains(text(),'Click for JS Prompt')]").click()
        time.sleep(2)
        # switch to the alert
        jsprompt = driver.switch_to.alert

        # send custom text to the prompt using send_keys( ) method
        jsprompt.send_keys('Nhan')

        # accept the alert
        jsprompt.accept()

        # assert that the result returned is what we expected
        textReturned = driver.find_element_by_id('result')

        print(textReturned.text)

        self.assertTrue(textReturned.text, 'You entered: Nhan')
        # screen shots
        destinationFilename = "C:\\workspace_python\\selenium\\switchto\\"
        tss.takeScreenshot(driver, destinationFilename)
        driver.quit()
ff = SwitchToAlert()
ff.testPromt()