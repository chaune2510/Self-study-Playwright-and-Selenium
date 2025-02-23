import time

class takeScreenShot():

    def takeScreenshot(self,driver,destination):
        filename = destination + str(round(time.time() * 1000)) + ".png"
        try:
            driver.save_screenshot(filename)
            print("Screenshot are save in dir: "+ filename)
        except NotADirectoryError:
            print("Not a directory issue!")