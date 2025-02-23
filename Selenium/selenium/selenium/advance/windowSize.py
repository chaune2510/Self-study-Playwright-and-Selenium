"""
height = return window.innerHeight;
width = return window.innerWidth;
"""
from selenium import webdriver
from utilities.takescreenshot import takeScreenShot
class windowSize():
    def testMethod(self):
        tss = takeScreenShot()
        #initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        #driver.maximize_window()
        #open the browers
        driver.get("https://the-internet.herokuapp.com/login")
        driver.implicitly_wait(10)
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))
        #screen shots
        destinationFilename= "C:\\workspace_python\\selenium\\advance\\"
        tss.takeScreenshot(driver,destinationFilename)
        driver.quit()
ff = windowSize()
ff.testMethod()