from splinter import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

import os
from pathlib import Path

import sys

import re

url = "https://www.contraloria.gov.co/control-fiscal/responsabilidad-fiscal/control-fiscal/responsabilidad-fiscal/certificado-de-antecedentes-fiscales/persona-natural"
id_number = 123456789

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def scrap_url(url, id_number):
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    # Visit URL

    #browser.visit(url)

    driver.get(url)
    wait = WebDriverWait(driver, 10)
    
    #browser.fill("ctl00$MainContent$ddlTipoDocumento", 1)

    iframe = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(iframe)
    select = Select(driver.find_element_by_id("ddlTipoDocumento"))

    #wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'ddlTipoDocumento')))
    #select = Select(wait.until(EC.element_to_be_clickable((By.ID, "ddlTipoDocumento"))))
    #choice = driver.find_element_by_xpath("//select/option[@value='1']")
    
    select.select_by_value("1")
    
    #choice.click()
    #browser.fill('txtNumeroDocumento', 123456789)
    
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
    new_path = path2file.rename(Path(path2file.parent, f"{path2file.stem}_{dt_string}{path2file.suffix}"))
    print(new_path)
n = len(sys.argv)
if(n==1):
    scrap_url(url, id_number)
elif(n==2):
    if(re.search(".csv", sys.argv[1])!=None):
        print("Read de database")
    else:
        scrap_url(url, sys.argv[1])
