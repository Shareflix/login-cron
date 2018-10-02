from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/abhayraizada/Downloads/chromedriver')
driver.get("https://netflix.com/in/login")
elem = driver.find_element_by_id("id_userLoginId")
elem.send_keys("toabhayraizada@gmail.com")
elem = driver.find_element_by_id("id_password")
elem.send_keys("ID0ntknow")
elem = driver.find_element_by_class_name("login-button")
elem.click()
