from models.Restaurante import Restaurante
from models.cardapio.Bebida import Bebida
from models.cardapio.Prato import Prato
import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurantes = {}
    for item in dados_json:
        nome_restaurante = item['Company']

        if nome_restaurante not in dados_restaurantes:
            dados_restaurantes[nome_restaurante] = []

        dados_restaurantes[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "descricao": item['description']
        })
else:
    print(response.status_code)




# Criação --> Cada arquivo, um restaurante com seu cardápio (itens)
    
# for nome_restaurante, dados in dados_restaurantes.items():
#     nome_arquivo = f'{nome_restaurante}.json'
#     with open(nome_arquivo, 'w') as arquivo_restaurante:
#         json.dump(dados, arquivo_restaurante, indent=4)


