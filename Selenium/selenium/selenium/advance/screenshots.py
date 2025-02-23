from selenium import webdriver
from utilities.takescreenshot import takeScreenShot
class screenShots():
    def testMethod(self):
        tss = takeScreenShot()
        #initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        #open the browers
        driver.get("https://the-internet.herokuapp.com/login")
        #use ID
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("tomsmith")
        #use Name
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("SuperSecretPasswor!")
        #click button
        driver.find_element_by_xpath("//button[@type='submit']").click()
        #screen shots
        destinationFilename= "C:\\workspace_python\\selenium\\advance\\"
        tss.takeScreenshot(driver,destinationFilename)
        #try:
        #    driver.save_screenshot(destinationFilename)
        #    print("Screenshots saved to dir:" + destinationFilename)
        #except NotADirectoryError:
        #    print("Not a directory issue!")
ff = screenShots()
ff.testMethod()