from splinter import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Este es un comentario, intento 2

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

# Visit URL
url = "https://www.contraloria.gov.co/control-fiscal/responsabilidad-fiscal/control-fiscal/responsabilidad-fiscal/certificado-de-antecedentes-fiscales/persona-natural"
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
driver.find_element_by_id('txtNumeroDocumento').send_keys('123456789')

# Find and click the 'search' button
button = driver.find_element_by_id('btnBuscar')
# Interact with elements

button.click()
time.sleep(10)
driver.close()

