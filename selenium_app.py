import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get('https://www.roblox.com/')
month_input = driver.find_element(by=By.ID, value='MonthDropdown')
day_input = driver.find_element(by=By.ID, value='DayDropdown')
year_input = driver.find_element(by=By.ID, value='YearDropdown')
username_input = driver.find_element(by=By.ID, value='signup-username')
password_input = driver.find_element(by=By.ID, value='signup-password')
male_button = driver.find_element(by=By.ID, value='MaleButton')
female_button = driver.find_element(by=By.ID, value='FemaleButton')
signup_button = driver.find_element(by=By.ID, value='signup-button')
month_input.send_keys('Mar')
day_input.send_keys('29')
year_input.send_keys('2000')
username_input.send_keys('Mziuri2024GITA_0')
password_input.send_keys('PasswordGita01')
male_button.click()

time.sleep(10)

signup_button.click()

time.sleep(10)

