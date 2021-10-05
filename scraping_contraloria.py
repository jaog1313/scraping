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





def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def scrap_url(url, id_number):
    driver = webdriver.Chrome()

    # Visit URL
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    iframe = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(iframe)
    select = Select(driver.find_element_by_id("ddlTipoDocumento"))
    select.select_by_value("1")
    driver.find_element_by_id('txtNumeroDocumento').send_keys(id_number)
    
    # Find and click the 'search' button
    button = driver.find_element_by_id('btnBuscar')
    
    # Interact with elements
    button.click()
    time.sleep(10)
    driver.close()

    #Search the file
    path2file = Path(find(id_number+".pdf", Path.home()))
    print(path2file)

    #Change the file's name
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    path2id_folder = os.path.join(Path.home(), id_number)
    if(os.path.exists(path2id_folder)==False):
        os.mkdir(path2id_folder)
    new_path = path2file.rename(Path(Path(path2id_folder), f"{path2file.stem}_{dt_string}{path2file.suffix}"))
    print(new_path)

if __name__ == "__main__":

    url = "https://www.contraloria.gov.co/control-fiscal/responsabilidad-fiscal/control-fiscal/responsabilidad-fiscal/certificado-de-antecedentes-fiscales/persona-natural"
    id_number = 123456789

    n = len(sys.argv)
    if(n==1):
        scrap_url(url, id_number)
    elif(n==2):
        if(re.search(".csv", sys.argv[1])!=None):
            print("Read de database")
        else:
            scrap_url(url, sys.argv[1])
