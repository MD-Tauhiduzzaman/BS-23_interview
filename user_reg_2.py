from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver= webdriver.Chrome(r"resource/chromedriver.exe")
url = "http://automationpractice.com/index.php"
driver.get(url)

driver.maximize_window()
time.sleep(2)
driver.find_element_by_partial_link_text("Sign").click()

driver.find_element_by_css_selector("#email_create").send_keys("tauhidshuvo01@gmail.com")
driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/button[1]/span[1]").click()
time.sleep(5)
driver.find_element_by_id("id_gender1").click()
driver.find_element_by_css_selector("#customer_firstname").send_keys("MD")
driver.find_element_by_css_selector("#customer_lastname").send_keys("Tauhiduzzaman")
driver.find_element_by_css_selector("#passwd").send_keys("ABCDE")

time.sleep(3)
day= Select(driver.find_element_by_css_selector("#days"))
day.select_by_value('1')
time.sleep(3)

month= Select(driver.find_element_by_css_selector("#months"))
month.select_by_value('1')
time.sleep(3)

year= Select(driver.find_element_by_css_selector("#years"))
year.select_by_value("1994")
time.sleep(3)
driver.find_element_by_css_selector("#newsletter").click()
driver.find_element_by_css_selector("#optin").click()
driver.find_element_by_css_selector("#firstname").send_keys("MD.")
driver.find_element_by_css_selector("#lastname").send_keys("Tauhiduzzaman")
driver.find_element_by_css_selector("#company").send_keys("ABC Limited")
driver.find_element_by_css_selector("#address1").send_keys("Dhaka")
driver.find_element_by_css_selector("#address2").send_keys("Dhaka")
driver.find_element_by_css_selector("#city").send_keys("Dhaka")

State= Select(driver.find_element_by_css_selector("#id_state"))
State.select_by_value('2')
time.sleep(3)

driver.find_element_by_css_selector("#postcode").send_keys("12000")
time.sleep(3)

#country= Select(driver.find_element_by_css_selector("#id_country"))
#country.select_by_value('1')
#time.sleep(3)


driver.find_element_by_css_selector("#other").send_keys("2nd Floor")
driver.find_element_by_css_selector("#phone").send_keys("123456789")
driver.find_element_by_css_selector("#phone_mobile").send_keys("123456789")
driver.find_element_by_css_selector("#other").send_keys("2nd Floor")

driver.find_element_by_css_selector("#alias").send_keys("Dhaka,BD")
driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[4]/button[1]/span[1]").click()