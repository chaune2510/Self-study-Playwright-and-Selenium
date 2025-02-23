from selenium import webdriver
class RunFFTest():
    def testMethod(self):
        #initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        #open the browers
        driver.get("https://the-internet.herokuapp.com/login")

ff = RunFFTest()
ff.testMethod()