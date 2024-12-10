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

Sign_in = driver.find_element_by_xpath('//*[@id="t2"]')
Sign_in.click()

time.sleep(4)

view_profile = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[1]/a')
view_profile.click()
time.sleep(3)

edit_button = driver.find_element_by_class_name('edit_button')
edit_button.click()
time.sleep(2)

enter_name = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/input')
enter_name.click()
enter_name.send_keys(' new name')
time.sleep(2)

enter_mobilenumber = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[5]/div/div[2]/input')
enter_mobilenumber.click()
enter_mobilenumber.send_keys('11111')

time.sleep(3)

save_button = driver.find_element_by_class_name('save_button_text')
save_button.click()

time.sleep(5)
driver.quit()


