from selenium import webdriver
# Importa la clase del Service y el tipo de WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv("config.env")

#driver = webdriver.Chrome()
driver: WebDriver = webdriver.Edge()#mejor declarar explicito que driver es de tipo WebDriver

driver.get(os.getenv("LICHESS_PAGE") or "")
driver.maximize_window()
time.sleep(5)
#usuario = driver.find_element(By.CLASS_NAME, "button button-empty signin")
usuario = driver.find_element(By.CSS_SELECTOR, ".button.button-empty.signin")
#tambien se puede driver.find_element(By.NAME)
usuario.click()
time.sleep(5)
driver.quit()
print("Terminado")
