from selenium import webdriver
import os

class RunIETest():
    def testIE(self):
        driverLocation="C:\\python\\browsers\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        driver = webdriver.Ie(driverLocation)
        driver.get("https://the-internet.herokuapp.com/login")

runIE = RunIETest()
runIE.testIE()