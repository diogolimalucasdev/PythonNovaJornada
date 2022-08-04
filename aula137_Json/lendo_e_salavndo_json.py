from aula137_Json.dados import *
import json

"abrindo um arquivo e transformando meu dicionario para json e salvando no meu arquivo em que eu abri"
# with open('clientes.json', 'w') as arquivo:
# #     json.dump(clientes_dicionario, arquivo, indent=4)

"agora eu vou ler o meu arquivo que esta em json e transformar para dicionario"
with open('clientes.json', 'r') as arquivo:
    dados_dicionario = json.load(arquivo)

for chave, valor in dados_dicionario.items():
    print(chave,valor)