from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver= webdriver.Chrome(r"resource/chromedriver.exe")
url = "http://automationpractice.com/index.php"
driver.get(url)

driver.maximize_window()
time.sleep(2)

