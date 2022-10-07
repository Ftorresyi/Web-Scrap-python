import pandas as pd
from main import * #importa o arquivo main dessa pasta com todas suas variaveis automaticamente.

#Passo 4: Atualizar a base de preços (atualializando preço de compra e venda usando a cotação obtida no Google)

#abrir a tabela produtos
tabela = pd.read_excel("Produtos.xlsx")
#print(tabela)

#atualizar a coluna cotação, onde a coluna Moeda for dólar
tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = float(cotacao_dolar)
print(tabela["Cotação"])
#molde: tabela.iloc["linha", "coluna"] - iloc localiza por linha e coluna
# No lugar da linha está sendo criada uma condição sem usar o if, pois o pandas faz isso automaticamente
#O código acima localiza a cotação das linhas onde a coluna moeda for igual a dólar 
# e atualiza com o valor da cotação obtida no goole pela variavel cotacao_dolar.
#Para editar uma linha em todas as colunas basta usar o ":" no lugar da coluna. Ficaria assim:
#tabela.loc[tabela["Moeda"]=="Dólar", :] = float(cotacao_dolar)

#atualizar a coluna preço de compra (=preço original * cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

#atualizar a coluna preço de venda (=preço original * cotação)
tabela["Preço de Venda"] = tabela["Preço Original"] * tabela["Cotação"]

print (tabela)

#Passo 5 Exportar a base de preços atualizada
tabela.to_excel("Resultado Produtos.xlsx", index=False)
#index=False exclui a coluna index da planilha