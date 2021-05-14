#library call
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

tiempo_vista = 10

navegador = webdriver.Edge(executable_path='msedgedriver.exe')
url = 'https://facebook.com'
navegador.get(url)

#ingresamos datos
user = WebDriverWait(navegador, 20).until(
    EC.presence_of_element_located((By.NAME, 'email')))
user.send_keys('2254533331')

pas = WebDriverWait(navegador, 20).until(
    EC.presence_of_element_located((By.NAME, 'pass')))
pas.send_keys('contravlady')

login_btn = WebDriverWait(navegador, 20).until(
    EC.presence_of_element_located((By.NAME, 'login')))
login_btn.click()

######## Vamos a la pagina #########

btn_2 = WebDriverWait(navegador, 20).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="mount_0_0_nQ"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[2]/span/div/a/span')))
btn_2.click()


#sleep(tiempo_vista)
#navegador.quit()
