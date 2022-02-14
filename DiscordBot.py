# import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

message = str(input("Enter your message: "))

PATH = "YOUR PATH" # Set PATH to ChromeDriver
driver = webdriver.Chrome(PATH) # Setting our driver

driver.get('https://discord.com/login') # Opening our login page

# Entering login info
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input").send_keys("USERNAME")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input").send_keys("PASSWORD")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]").click()

time.sleep(5) # Waiting for page to load
driver.get("URL OF DIRECT MESSAGE")

time.sleep(5) # Waiting for page to load
driver.find_element_by_xpath("XPATH OF DIRECT MESSAGE TEXT FIELD").send_keys(message, Keys.ENTER) # Sending message
