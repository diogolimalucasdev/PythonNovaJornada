"""
JavaScript Object Notation - Json
Json(JavaScript Object Notation) é um formato de troca de dados entre sistemas e programa
muito leve e de fácil utilização. Muito uitlizado por APIs
"""

"documentação:https://docs.python.org/3/library/json.html"

from aula137_Json.dados import *
import json

"convertendo minha lista para json"
lista = [1,2,3,4,5,6,7]
dados_json = json.dumps(lista)
print(type(dados_json))

"convertendo dicionario para json e uso o indent=4 para visualizar melhor"
dados_json2 = json.dumps(clientes_dicionario, indent=4)
print(dados_json2)


"convertendo de json para dicionario"
dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave, valor)