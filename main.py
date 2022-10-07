import os
from selenium import webdriver #permite criar o navegador
from selenium.webdriver.common.keys import Keys #permite escrever no navegador
from selenium.webdriver.common.by import By #permite selecionar itens no navegador

#Configura do local do WebDriver
chromedriver = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.10\chromedriver.exe"
#Seta a variável ambiente do Chromedriver
os.environ["webdriver.chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)
#driver.get("http://stackoverflow.com")


'''# Para acessar o navegador em segundo plano, sem ficar à vistas, usar:
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(chromedriver, options=chrome_options)'''
#Porém, vamos usar a opção de usar tudo no primeiro plano para ajudar a ver o que está acontecendo.

#Passo 1: Pegar cotação do dólar:
#navegador = webdriver.Chrome() #abrir o navegador. Não fiz dessa forma, pois deu erro na minha máquina

#entrar no google
driver.get("http://www.google.com.br")

#pesquisar no google por "cotação dólar"
driver.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
driver.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) # Pressiona a tecla Enter.
#encontra o elemento através do XPATH
#Para isso basta clicar com o botão direito no navegador em "inspecionar e encontrar o código do elemento buscado"
#Ao passar o mouse na tela, o código relacionado fica em azul. 
#Depois disso, basta copiá-lo aqui, clicando na opção copiar XPATH na página e colar aqui.
#send_keys escreve na tela do goole, no local que indicamos
#vantagem do selenium é que ele espera a página carregar automaticamente, assim não precisa programar o tempo de espera.
#Macete: Sempre usar aspas simples para XPATH, pois se houver aspas duplas dentro do caminho pode causar erro.

#pegar o valor da cotação do google
cotacao_dolar = driver.find_element("xpath",'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar, type(cotacao_dolar))

driver.quit()

