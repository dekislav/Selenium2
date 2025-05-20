from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#Set up the webdriver
driver = webdriver.Chrome()
try:

    driver.get("file:///C:/Users/dejan/Desktop/selenium day2/Selenuim2/Dashboard.html")

    time.sleep(2)

    #TestCase001: Check if the welcome message is displayed
    # header = driver.find_element(By.TAG_NAME, "h1")
    # assert "Welcome, Thabelo!=" in header.text
    # print("Welcome message is displayed")
    #TestCase002: Check if the logout button exists
    # logout_btn = driver.find_element(By.CLASS_NAME,"logout-btn")
    # assert logout_btn.is_displayed() and logout_btn.is_enabled()
    # print("The logout button exists!")
    #TestCase003:Type in Searchbox 
    #testcase004
    
    #searchbox = driver.find_element(By.ID,"search-box")

    #assert searchbox.is_displayed()

    #searchbox.send_keys("It works")

    #print("The searchbox is functional")
    #calender_input = driver.find_element(By.ID,"calendar")
    #calender_input.send_keys("24/08/2025")
    #print("Successfuly chnaged the date")
    #testcase005 find image
    buggy = driver.find_element(By.CSS_SELECTOR, ".profile-img img ")
    assert buggy.get_attribute("src")!=""
    print("Buggy has been found")
except AssertionError as e:

    print("Test failed:",e)

except Exception as e:

    print("Error occurred:",e)

finally:

    time.sleep(2)

    driver.quit()
 