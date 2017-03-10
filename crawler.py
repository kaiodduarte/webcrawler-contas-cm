import os
from selenium import webdriver
from time import sleep

driver_path = os.path.join(os.getcwd(), 'chromedriver')
url = 'https://campomourao.atende.net/?pg=transparencia#!/grupo/2/item/8/tipo/1'

# Abre o Google Chrome, maximiza a janela e abre o link
driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get(url)

sleep(1)
css_selector = 'div[class="titulo"] button'
driver.find_element_by_css_selector(css_selector).click()

sleep(2)
css_consulta = 'span[class="label_botao_acao"]'
driver.find_element_by_css_selector(css_consulta).click()

with open('cm.txt', 'a') as file:
    tag = ''
    while (tag != 'desativado'):
        sleep(2)
        css_next_page = 'span[title="Próxima Página"]'
        aux = driver.find_element_by_css_selector(css_next_page)
        tag = aux.get_attribute('class')[-10:]
        
        sleep(2)
        css_tabela = 'table[class="dados_consulta dados"]'
        despesas = driver.find_element_by_css_selector(css_tabela).text.split('\n')[:-3]

        if (tag != 'desativado'):
            aux.click()
    
        for despesa in despesas:
            file.write(despesa + '\n')
