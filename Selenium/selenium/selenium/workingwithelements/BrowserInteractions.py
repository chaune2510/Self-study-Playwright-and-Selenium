from selenium import webdriver

class BroswerInteractions():
    def test(self):
        baseURL="http://formy-project.herokuapp.com/form"
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #maximize windows
        driver.maximize_window()
        #open URL
        driver.get(baseURL)
        #get tilte
        strTitle = driver.title
        print(strTitle)
        print("*************************")
        #get URL
        strURL = driver.current_url
        print(strURL)
        print("*************************")
        strSource = driver.page_source
        print(strSource)
        driver.quit()

BI = BroswerInteractions()
BI.test()