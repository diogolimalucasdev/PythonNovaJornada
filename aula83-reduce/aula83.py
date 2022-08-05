from functools import reduce
from aula137_Json.dados import  lista, pessoas, produtos

#acumuladora compulsiva, acumuladora de valores
acumula = 0
for item in lista:
    acumula += item
print(acumula)

#usando o lambda
soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
print(soma_lista)

soma_preco = reduce(lambda acumulador2, produto: produto['preco'] + acumulador2, produtos, 0)
print(soma_preco)


acumulador_2 = 0
for item in produtos:
    acumulador_2 += item['preco']
print(acumulador_2)


#usando lambda
acumulador3 = 0
soma_idade = reduce(lambda acumulador3, pessoas: int(pessoas['idade']) + acumulador3, pessoas, 0 )
print(soma_idade)

#usando o for
acumulador_3 = 0
for idade in pessoas:
    acumulador_3 += int(idade['idade'])
print(acumulador_3)
