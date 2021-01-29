import requests
import json 
import pandas as pd
from pandas import DataFrame
import os

norte = 0
nordeste = 0
sudeste = 0
sul = 0
centroOeste = 0
lista = []

dados = requests.get(' https://servicodados.ibge.gov.br/api/v1/localidades/estados/')

frame = json.loads(dados.text)

for i in range (len(frame)):
    if (frame[i]['regiao']['nome'] == "Norte"):
        norte +=1
    elif (frame[i]['regiao']['nome'] == "Nordeste"):
        nordeste +=1
    elif (frame[i]['regiao']['nome'] == "Sudeste"):
        sudeste +=1
    elif (frame[i]['regiao']['nome'] == "Sul"):
        sul +=1
    elif (frame[i]['regiao']['nome'] == "Centro-Oeste"):
        centroOeste +=1

lista.append(norte)
lista.append(nordeste)
lista.append(sudeste)
lista.append(sul)
lista.append(centroOeste)

frame2 = DataFrame(["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"], columns = ["Região"])
frame2["Qtd. Estados"] = lista

print (frame2)


if (os.path.isdir("IBGE")):
    print("\nPasta IBGE já existe.")
else:
    os.mkdir("IBGE")
    print("\nPasta IBGE criada.")

frame2.to_csv("IBGE/ibge.csv", sep="|", index=False)

print("\nGerado o arquivo IBGE/ibge.csv")

