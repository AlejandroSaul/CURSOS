"""
Antes :
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "../Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://lichess.org/")
driver.close()"""

from selenium import webdriver
import time

#driver = webdriver.Chrome()
driver = webdriver.Edge()

driver.get("https://lichess.org/")
driver.maximize_window()
time.sleep(5)
driver.quit()
print("Terminado")