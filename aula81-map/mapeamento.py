from dados import produtos , pessoas , lista

print(lista)

# mapeamento
nova_lista = map(lambda x: x * 2 , lista)  # em cada elemento da minha lista ele vai executar minha função lambda
print(list(nova_lista))


# com list compheention
# nova_lista2 = [x * 2 for x in lista]
# print(nova_lista2)


# aplicar 5% nos valores dos meus produtos do dicionario
def aumenta_preco(produto):
    produto['preco'] = round(produto['preco'] * 1.05 , 2)  # aqui eu altero o valor de cada produto
    return produto


novos_precos = map(aumenta_preco , produtos)  # a cada linha do meu dicionario eu passei minha função aumenta preco
for produto in novos_precos:
    print(produto)

# buscando apenas os nomes
nomes = map(lambda p: p['nome'] , pessoas)
for pessoa in nomes:
    print(pessoa)

# aumentando as idades das pesoas
idades = map(lambda idade: idade['idade'] , pessoas)
for idade in idades:
    print(idade)
