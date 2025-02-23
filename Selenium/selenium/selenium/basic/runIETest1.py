from selenium import webdriver


class RunIETest():
    def testIE(self):
        driverLocation="C:\\python\\browsers\\msedgedriver.exe"
        #os.environ["webdriver.edge.driver"] = driverLocation
        driver = webdriver.Edge(executable_path="C:\\python\\browsers\\MicrosoftWebDriver.exe")
        driver.get("https://the-internet.herokuapp.com/login")

runIE = RunIETest()
runIE.testIE()