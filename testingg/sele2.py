from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.easyclass.com/login')
user_name = "viyashsasi@gmail.com"
pwd = "Sasirekha*19"
email= driver.find_element_by_name("email")
email.send_keys(user_name)
pword= driver.find_element_by_name("password")
pword.send_keys(pwd)
login_box = driver.find_element_by_name('submit')
login_box.click()
driver.quit
