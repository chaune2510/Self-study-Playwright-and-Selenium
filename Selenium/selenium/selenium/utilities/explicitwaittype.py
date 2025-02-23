from traceback import print_stack

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.findElements import findElements

class ExplicitWaitType():

    def __init__(self,driver):
        self.driver = driver
        self.fe = findElements(driver)

    def waitForElement(self,locator, locatortType="id",timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.fe.getByType(locatortType)

            wait = WebDriverWait(self.driver,timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,locator)))
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element