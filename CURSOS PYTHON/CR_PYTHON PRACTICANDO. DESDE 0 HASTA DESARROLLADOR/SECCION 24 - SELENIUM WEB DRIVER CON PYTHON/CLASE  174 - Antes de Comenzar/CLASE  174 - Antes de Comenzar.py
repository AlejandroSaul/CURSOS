from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv("config.env")

driver = webdriver.Edge()

driver.get(os.getenv("LICHESS_PAGE"))
driver.maximize_window()

time.sleep(3)

login = driver.find_element(By.CSS_SELECTOR, ".button.button-empty.signin")
login.click()

time.sleep(5)

usuario = driver.find_element(By.ID, "form3-username")
usuario.send_keys(os.getenv("LICHESS_USUARIO"))

clave = driver.find_element(By.ID, "form3-password")
clave.send_keys(os.getenv("LICHESS_PASS"))

time.sleep(2)

inicio = driver.find_element(By.CSS_SELECTOR, "button.submit.button")
inicio.click()

time.sleep(5)

driver.quit()