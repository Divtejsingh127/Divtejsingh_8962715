from telnetlib import EC

import driver
from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Open a Chrome browser
driver = webdriver.Chrome()

# Navigate to the Poparide website
driver.get("https://www.poparide.com/")

# Find and interact with elements on the website
#element_list = driver.find_elements_by_xpath("//a")[:4]  # Select the first 4 elements
#for element in element_list:
    #print(element.text)  # Print the text of each element



# Wait for 5 seconds instead of 2 seconds
time.sleep(3)

# Click the "Find a Ride" button
find_ride_button = driver.find_element("xpath","/html/body/div[4]/div/div[1]/a[1]")
find_ride_button.click()

time.sleep(3)

# Click the "From" tab (replace the XPath with the actual XPath of the tab)
from_tab_button = driver.find_element("xpath", "/html/body/div[5]/div[1]/div[1]/div[4]/div[1]/form/div[1]/div/input[1]")
from_tab_button.click()


time.sleep(3)

# Wait for the address input field to be present
address_input = driver.find_element("id","id_origin-modal-location-input")
address_input.send_keys("Ontario, Canada")

# Enter an address in the input field
address_input.send_keys(Keys.RETURN)

time.sleep(3)

#assert "Ontario,Canada" in driver.title

# Click on the selected address in the dropdown
address_link = driver.find_element("xpath","/html/body/div[14]/div/div[2]/div[4]/div[2]")
address_link.click()
time.sleep(5)

# Click the "To" tab (replace the XPath with the actual XPath of the tab)
To_tab_button = driver.find_element("xpath", "/html/body/div[5]/div[1]/div[1]/div[4]/div[1]/form/div[3]/div/input[1]")
To_tab_button.click()

time.sleep(3)

# Wait for the address input field to be present
destination_input = driver.find_element("id","id_destination-modal-location-input")
destination_input.send_keys("Ontario, Canada")

# Enter an address in the input field
destination_input.send_keys(Keys.RETURN)

time.sleep(3)

#assert "Ontario,Canada" in driver.title

# Click on the selected address in the dropdown
destination_link = driver.find_element("xpath","/html/body/div[14]/div/div[2]/div[4]/div[3]")
destination_link.click()
time.sleep(5)

#Click the search button
search_button = driver.find_element("id", "button-find")

search_button.click()

time.sleep(5)

#select first option
trip_link = driver.find_element("xpath","/html/body/div[5]/div[3]/div[2]/div[1]/div[3]/div[3]/div[4]/div[1]/div")
trip_link.click()
time.sleep(5)
# Close the browser
driver.quit