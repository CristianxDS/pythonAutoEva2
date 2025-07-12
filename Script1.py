from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.demoblaze.com/index.html"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

registro = driver.find_element(By.XPATH, '//*[@id="signin2"]')
driver.execute_script("arguments[0].click();", registro)
time.sleep(3)

usuario = "CristhiamSabandoITSQMET"
clave = "Contrania1234"

usuario_reg = driver.find_element(By.XPATH, '//*[@id="sign-username"]')
clave_reg = driver.find_element(By.XPATH, '//*[@id="sign-password"]')

usuario_reg.send_keys(usuario)
clave_reg.send_keys(clave)

boton_reg = driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
driver.execute_script("arguments[0].click();", boton_reg)
time.sleep(3)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alerta = driver.switch_to.alert
    alerta.accept()
except:
    print("No apareció alerta tras registrar")

time.sleep(3)

login = driver.find_element(By.XPATH, '//*[@id="login2"]')
driver.execute_script("arguments[0].click();", login)
time.sleep(3)

usuario_log = driver.find_element(By.XPATH, '//*[@id="loginusername"]')
clave_log = driver.find_element(By.XPATH, '//*[@id="loginpassword"]')

usuario_log.send_keys(usuario)
clave_log.send_keys(clave)

boton_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
driver.execute_script("arguments[0].click();", boton_login)
time.sleep(5)

prod1 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
prod1.click()
time.sleep(3)

agregar1 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
agregar1.click()
time.sleep(3)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alerta = driver.switch_to.alert
    alerta.accept()
except:
    print("No apareció alerta tras agregar primer producto")

driver.get(url)
time.sleep(3)

prod2 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/div/h4/a')
prod2.click()
time.sleep(3)

agregar2 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
agregar2.click()
time.sleep(3)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alerta = driver.switch_to.alert
    alerta.accept()
except:
    print("No apareció alerta tras agregar segundo producto")

time.sleep(5)
driver.quit()

