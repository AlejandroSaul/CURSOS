from selenium import webdriver
import time
from dotenv import load_dotenv
import os
"""
Antes :

driver = webdriver.Chrome(executable_path = "../Drivers/chromedriver.exe")
driver.maximize_window()
driver.get(os.getenv("LICHESS_PAGE"))
driver.close()

Ahora:
"""


load_dotenv("config.env")

#driver = webdriver.Chrome()
driver = webdriver.Edge()

driver.get(os.getenv("LICHESS_PAGE"))
driver.maximize_window()
time.sleep(5)
driver.quit()
print("Terminado")