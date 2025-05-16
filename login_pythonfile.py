import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# create a driver fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
#Test case execution
def test_login(driver):
    file_path = os.path.abspath("Login_Page.HTML")
    driver.get("file://" + file_path)
    #interact with the form
    driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail.com")
    driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
    driver.find_element(By.ID, "login-btn").click()
    #Wait for the popup to appear
    wait = WebDriverWait(driver, 10)
    popup = wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
    popup_message = driver.find_element(By.ID, "login-popup-message").text
    #assertions
    assert popup.is_displayed(), "Login did not display the popup"
    assert "successfully" in popup_message.lower(), f"Unexpected message: {popup_message}"
    time.sleep(2)




