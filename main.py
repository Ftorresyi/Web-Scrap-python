import os
from selenium import webdriver #permite criar o navegador
from selenium.webdriver.common.keys import Keys #permite escrever no navegador
from selenium.webdriver.common.by import By #permite selecionar itens no navegador

#Configura do local do WebDriver
chromedriver = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.10\chromedriver.exe"
#Seta a variável ambiente do Chromedriver
os.environ["webdriver.chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")

#Passo 1: Pegar cotação do dólar:
#navegador = webdriver.Chrome() #abrir o navegador. Não fiz dessa forma, pois deu erro na minha máquina
#entrar no google
#pesquisar no google por "cotação dólar"
#pegar o valor da cotação

