########################### HERRAMIENTAS Y LIBRERÍAS ##############################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

########################### INICIACIÓN DE WEBDRIVER ##############################

browser = webdriver.Chrome(executable_path = '/usr/bin/chromedriver')

browser.maximize_window()

browser.get('https://web.whatsapp.com/')
#Acá pedirá la validación del codigo QR de WhatsAppWeb... Pronto será corregido. 

time.sleep(5)

########################### LECTURA GRUPOS Y TEXTO  ##############################
	
with open('groups.txt', 'r', encoding='utf8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()


########################### SELECCIÓN Y ENVÍO DE MENSAJE ##############################

#Se utiliza un 'for' para que itere por cada elemento presente ambos archivos

for group in groups:
	# Seleccionamos la "ventana de busqueda" de los chats de WhatsApp con su descripción de div 
	# Para obtenerla debemos 'inspeccionar' la pag. de WhatsApp web	
	search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
	
	search_box = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.XPATH, search_xpath)))

	search_box.clear()
	
	search_box.send_keys(group)
	# Le damos segundos de espera entre procesos por cualquier delay en el navegador
	time.sleep(2)
	
	# Seleccionada la "ventana de busqueda" procedemos a extraer el nombre del grupo de 'groups.txt'
	group_xpath = f'//span[@title="{group}"]'
	group_title = browser.find_element_by_xpath(group_xpath)
	# Encontrado el grupo se selecciona (clickea)

	group_title.click()
	time.sleep(1)

	# Selección de la ventana de chat
	input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
	input_box = browser.find_element_by_xpath(input_xpath)

	# Pegado del mensaje definido en 'msg.txt'
	input_box.send_keys(msg)
	
	time.sleep(2)
