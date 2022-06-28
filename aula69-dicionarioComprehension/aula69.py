lista = [
        ('chave', 'valor'),
        ('chave2', 'valor2')
]

d1 = {x: y for x, y in lista} #transformo o que esta na lista em dicionario
d1 = dict(lista) #poderia fazer assim tambem que daria no mesmo
print(d1)

#mas se eu quiser fazer alguma alterção como essa por exemplo
lista2 = [
        ('chave', 2),
        ('chave2', 3)
]
d2 = {x:y*2 for x, y in lista2} #estou multiplicando todos os valores da chave por 2
print(d2)

d3 = {f'chave_{x}': x**2 for x in range(5)} #criando o dicionario com chave e valor utilizando f string e range
print(d3)