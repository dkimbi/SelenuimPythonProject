from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/bin/chromedriver"  # Update the path to the correct location of chromedriver on your system
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")

link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "python website"))
    )
    element.click()

    # Go back
    driver.back()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Classes and Objects"))
    )
    element.click()

    driver.back()

    driver.back()

    driver.forward()

finally:
    driver.quit()
