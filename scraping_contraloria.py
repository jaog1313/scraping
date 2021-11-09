import os
import sys
import re
import time
from datetime import datetime
from selenium import webdriver
from splinter import Browser
from pathlib import Path
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
'''
Requerimientos:
1. Usar librerias como scrapy o beautifulsoup?
2. Si uno observa el comportamiento de la página se da cuenta de que no se 
	necesita hacer scraping siempre
3. Debe correr desde un servidor. Sin interfaz gráfica. Escalabilidad.
4. Tomar el tiempo.
5. Documentación
6. Archivo de configuracion o requirements.
7. Hacer todos los comentarios en español
8. Se deben manejar excepciones
	2.1. ¿Qué pasa si la página está caída?
	2.2. ¿Qué pasa si no devuelve un pdf?
	2.3. ¿Si pongo las cédulas en una cola cómo sé que ya acabó con
		una cédula?


'''

def type_id_str(num):
    '''
    Devuelve segun sea el caso el tipo de documento.
    Esta basado en la pagina de la Contraloria
    '''
    switch = {
            "1": "CC", #Cedula de ciudadania
            "2": "CE", #Cedula de extranjeria
            "3": "TI", #Tarjeta de identidad
            "4": "PAS", #Pasaporte
            "5": "PEP" #Permiso Especial de Permanencia
            }
    return switch.get(num, "Entrada no valida")

def find(nombre, path):
    '''
    Encuentra un archivo con el nombre nombre, empezando la busqueda desde el directorio path
    '''
    for root, dirs, files in os.walk(path):
        if nombre in files:
            return os.path.join(root, nombre)

def scrap_url(url, id_number, type_id):
    '''
    Scraping la url dada.
    Basados en el html de contraloria.gov.co
    '''
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Visit URL
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    iframe = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(iframe)
    select = Select(driver.find_element_by_id("ddlTipoDocumento"))
    select.select_by_value(type_id)
    driver.find_element_by_id('txtNumeroDocumento').send_keys(id_number)
    
    # Find and click the 'search' button
    boton = driver.find_element_by_id('btnBuscar')
    
    # Interact with elements
    boton.click()
    time.sleep(10)
    driver.close()

    #Search the file
    path2file = Path(find(id_number+".pdf", Path.home()))
    print(path2file)

    #Change the file's name
    ahora = datetime.now()
    dt_string = ahora.strftime("%d_%m_%Y_%H_%M_%S")
    path2id_folder = os.path.join(Path.home(), f"{type_id_str(type_id)}_{id_number}")
    if(os.path.exists(path2id_folder)==False):
        os.mkdir(path2id_folder)
    new_path = path2file.rename(Path(Path(path2id_folder), f"{type_id_str(type_id)}_{path2file.stem}_{dt_string}{path2file.suffix}"))
    print(new_path)


if __name__ == "__main__":
    url = "https://www.contraloria.gov.co/control-fiscal/responsabilidad-fiscal/control-fiscal/responsabilidad-fiscal/certificado-de-antecedentes-fiscales/persona-natural"
    id_number = 123456789
    n = len(sys.argv)
    if(n==1):
        scrap_url(url, id_number, "1")
    elif(n==2):
        if(re.search(".csv", sys.argv[1])!=None):
            print("Read the database")
        else:
            scrap_url(url, sys.argv[1], "1")
    elif(n==3):
            scrap_url(url, sys.argv[1], sys.argv[2])
