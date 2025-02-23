"""
# Scroll Down
window.scrollBy(0, 1000);
# Scroll Up
window.scrollBy(0, -1000);
# Scroll Element Into View
element = driver.find_element(By.ID, "")
arguments[0].scrollIntoView(true);", element)
window.scrollBy(0, -150);
# Native Way To Scroll Element Into View
window.scrollBy(0, -1000);
window.scrollBy(0, -150);
"""
import time

from selenium import webdriver
from utilities.takescreenshot import takeScreenShot
class Scrolling():
    def testMethod(self):
        tss = takeScreenShot()
        #initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        driver.maximize_window()
        #open the browers
        driver.get("http://formy-project.herokuapp.com/scroll")
        driver.implicitly_wait(10)
        # Scroll Down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(4)
        # Scroll Up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)
        # Scroll Element Into View
        fullname = driver.find_element_by_id("name")
        driver.execute_script("arguments[0].scrollIntoView(true);",fullname)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-150);")
        # Native Way To Scroll Element Into View
        driver.execute_script("window.scrollBy(0,-1000);")
        location = fullname.location_once_scrolled_into_view
        print("Location: " +str(location))
        time.sleep(2)
        #screen shots
        destinationFilename= "C:\\workspace_python\\selenium\\advance\\"
        tss.takeScreenshot(driver,destinationFilename)
        driver.quit()
ff = Scrolling()
ff.testMethod()