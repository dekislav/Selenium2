import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

#loggin configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='login_test.log',
    filemode='w'
)

def test_login_popup(driver):
    file_path = os.path.abspath("Login_Page.html")
    logging.info("Opening File: %s", file_path)
    driver.get("file://" + file_path)
    try:
        #test case 1 valid details
        logging.info("Enter email and password")
        #driver.find_element(By.CLASS_NAME, "email"). send_keys("Selenium25@gmail.com")
        #driver.find_element(By.CLASS_NAME, "password"). send_keys("Y0uMade1t&3&&")
        #driver.find_element(By.ID, "login-btn").click()
        #test case 003
        
        #take a screenshot
        driver.save_screenshot("screenshot_before_popup.png")
        logging.info("screenshot saved berfore popup appears")
        #wate for popup and validate
        wait = WebDriverWait(driver,10)
        popup = wait.until(EC.visibility_of_element_located((By.ID,"login-popup")))
        popup_message = driver.find_element(By.ID, "login-popup-message").text
        logging.info("Popup message:%s" ,popup_message)
        #assert behavior
        assert popup. is_displayed(), "Login did not display the popup"
        assert "successfully" in popup_message.lower(),f"unexpected message: {popup_message}"
        logging.info("Login popup test passsed on: %s", driver.name )
        #time.sleep(5)
        #error handling
    except Exception as e:
        logging.error("An error occured during testing:%s",e)
        driver.save_screenshot("error screenshoot.png")
        raise
#run the test
chrome_driver = webdriver.Chrome()
test_login_popup(chrome_driver)
chrome_driver.quit()