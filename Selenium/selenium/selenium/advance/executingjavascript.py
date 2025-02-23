"""
driver.execute_script("some javascript code here");

driver.execute_script("window.location = '';")

driver.execute_script("return document.getElementById('name');")

javaScript = "document.getElementsByName('username')[0].click();"
driver.execute_script(javaScript)

functions getElementsByName ,  getElementsByClassName , and so on return all matching elements as an array.
function ' getElementById ', you do not need to use any indexing, as it will return only one element (‘id’ should be unique)

driver.execute_script("document.getElementById('firstname').click();")

userName = driver.find_element_by_xpath("//button[@type='submit']")
driver.execute_script("arguments[0].click();", userName)

arguments[0].value='SuperSecretPasswor!';"

"""
import time

from selenium import webdriver
from utilities.takescreenshot import takeScreenShot
class executingJavascript():
    def testMethod(self):
        tss = takeScreenShot()
        #initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        #open the browers
        #driver.get("https://the-internet.herokuapp.com/login")
        driver.execute_script("window.location='https://the-internet.herokuapp.com/login';")
        driver.implicitly_wait(10)
        #use ID
        username = driver.find_element_by_id("username")
        driver.execute_script("arguments[0].value='tomsmith';", username)
        #use Name
        #driver.find_element_by_id("password").clear()
        #driver.find_element_by_id("password").send_keys("SuperSecretPasswor!")
        password = driver.find_element_by_id("password")
        driver.execute_script("arguments[0].value='SuperSecretPasswor!';", password)

        #click button
        btnSubmit = driver.find_element_by_xpath("//button[@type='submit']")
        driver.execute_script("arguments[0].click();", btnSubmit)
        time.sleep(10)
        #screen shots
        destinationFilename= "C:\\workspace_python\\selenium\\advance\\"
        tss.takeScreenshot(driver,destinationFilename)

        driver.quit()

ff = executingJavascript()
ff.testMethod()