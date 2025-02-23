from selenium import webdriver
class RunFFTest():
    def testMethod(self):
        #initiate the driver
        driver = webdriver.Firefox(executable_path="C:\\python\\browsers\\geckodriver.exe")
        #open the browers
        driver.get("https://the-internet.herokuapp.com/login")
        #use ID
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("tomsmith")
        #use Name
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("SuperSecretPassword!")
ff = RunFFTest()
ff.testMethod()