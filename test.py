import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
print (DRIVER_BIN)


from selenium import webdriver
   
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
   
# create webdriver object
driver = webdriver.Chrome(DRIVER_BIN)
   
# get geeksforgeeks.org
driver.get("https://oportunidades.sofka.com.co/jobs/1254406-liga-de-entrenamiento-en-automatizacion-de-pruebas")
   
# get element 
element = driver.find_element_by_id("tt-cookie-alert__accept-all")
   
# create action chain object
action = ActionChains(driver)
   
# click the item
action.click(on_element = element)
   
# perform the operation
action.perform()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "js-menu-trigger sliding-menu-button burger-wrapper"))).click()