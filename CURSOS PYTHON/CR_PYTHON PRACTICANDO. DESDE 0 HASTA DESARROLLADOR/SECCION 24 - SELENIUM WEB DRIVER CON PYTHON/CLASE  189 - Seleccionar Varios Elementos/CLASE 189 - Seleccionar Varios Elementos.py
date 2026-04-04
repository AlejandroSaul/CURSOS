from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

#print("Ruta actual:", os.getcwd()) #get current working directory

load_dotenv("config.env")

#print("Valor:", os.getenv("CHESS_COM_PAGE"))

driver = webdriver.Edge()
print(os.getenv("CHESS_COM_PAGE"))
driver.get(os.getenv("CHESS_COM_PAGE"))
driver.maximize_window()

wait = WebDriverWait(driver, 10)
login = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                ".cc-button-component.cc-button-secondary.cc-bg-secondary.cc-button-medium.guest-activity-trackable.navbar-login"))
)

login.click()
wait.until(
    EC.visibility_of_element_located((By.ID, "login-username"))
)

varios = driver.find_elements(By.CSS_SELECTOR, "input.cc-input-component")

for i in varios:
    if i.is_displayed():
        i.send_keys("123456789")

time.sleep(5)

driver.quit()