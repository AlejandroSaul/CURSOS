from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os


load_dotenv("config.env")

driver = webdriver.Edge()

driver.get(os.getenv("LICHESS_PAGE"))
driver.maximize_window()

wait = WebDriverWait(driver, 10)
'''
login = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "button"))
) en caso de class solo acepta UNA clase, no múltiples.
'''
#<a href="/login?referrer=/" class="button button-empty signin">Iniciar sesión</a>
#son 3 clases diferentes: button button-empty signin
#El . indica que es una clase (igual que en CSS)
login = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.button-empty.signin"))
)
login.click()

usuario = wait.until(
    EC.presence_of_element_located((By.ID, "form3-username"))
)
usuario.send_keys(os.getenv("LICHESS_USUARIO"))

clave = wait.until(
    EC.presence_of_element_located((By.ID, "form3-password"))
)
clave.send_keys(os.getenv("LICHESS_PASS"))

inicio = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit.button"))
)
inicio.click()
time.sleep(5)

driver.quit()