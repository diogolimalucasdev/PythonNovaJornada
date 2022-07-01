"""
Considerando duas listas de inteiros ou floats (lista A e lista B) some os valores nas listas
retornando uma nova lista com os valores somados:

Se uma lista for amior que a outra, a soma vai considerar o tamanho da menor

Exemplo:

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

------------------------
lista_soma = [2, 4, 6, 8]

"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = zip(lista_b, lista_b)
lista_final = []

for soma in lista_soma:
    lista_final.append(soma[0] + soma[1])

print(lista_final)


###################################
"de outra forma"

lista_a2 = [1, 2, 3, 4, 5, 6, 7]
lista_b2 = [1, 2, 3, 4]

lista_soma2 = []
for i in range(len(lista_b2)):
    lista_soma2.append(lista_a2[i] + lista_b2[i])

print(lista_soma2)