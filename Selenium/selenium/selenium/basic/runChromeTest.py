from selenium import webdriver

class RunChromeTest():
    def testChrome(self):
        #initiate driver
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #open url
        driver.get("https://the-internet.herokuapp.com/login")

ch = RunChromeTest()
ch.testChrome()