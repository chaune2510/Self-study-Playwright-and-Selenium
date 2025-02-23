from selenium import webdriver
import time
class clickandtype():
    def test(self):
        baseURL="http://formy-project.herokuapp.com"
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #maximize windows
        driver.maximize_window()
        #open URL
        driver.get(baseURL)
        #click link form
        driver.find_element_by_xpath("//a[@href='/form']").click()
        time.sleep(5)
        #type to first name
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys("Tam")
        #type to last name
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys("Tran")

        #type to job title
        driver.find_element_by_id("job-title").clear()
        driver.find_element_by_id("job-title").send_keys("QC")
        #quit driver
        time.sleep(5)
        driver.quit()

ch = clickandtype()
ch.test()