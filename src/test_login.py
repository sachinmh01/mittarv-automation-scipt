import time
from selenium import webdriver

URL = 'https://app.mittarv.com/'
driver = webdriver.Firefox(executable_path="driver/geckodriver.exe")
driver.get(URL)
driver.maximize_window()
time.sleep(3)

enter_email = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/div/div/div[3]/input')
enter_email.click()
enter_email.send_keys('helangesachin96@gmail.com')
time.sleep(1)

sent_otp = driver.find_element_by_id('t2')
sent_otp.click()
time.sleep(40)

# Enter the OTP manually
# ############

enter_otp = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/input[1]')
enter_otp.click()
time.sleep(3)

sign_in = driver.find_element_by_xpath('//*[@id="t2"]')
sign_in.click()

time.sleep(4)

click_logout = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/p')
click_logout.click()


time.sleep(5)
driver.quit()


