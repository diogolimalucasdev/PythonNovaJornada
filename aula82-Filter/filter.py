from dados import lista , pessoas , produtos

# muito similiar ao map, tambem reecebe uma função, a diferença que o filter retornar True or false
nova_lista = filter(lambda x: x > 5 , lista)  # todos numeros que forem acima de 5 serao mantidos na nova_lista
print(list(nova_lista))

# em list comphention
nova_lista = [x for x in lista if x > 5]  # do mesmo jeito que eu fiz com filter
print(nova_lista)

# buscando valores acima de 50 reais nos meu diconario produto
produto_acima_50 = filter(lambda produtos: produtos['preco'] > 50 , produtos)

# como é um diccionario eu utilizo o for
print("\n Usando Lambda")
for produto in produto_acima_50:
    print(produto)


# agora utilizando uma função

def filtra(produto): #a função vai retornar ou None ou True(quando o valor for acima de 50)
    if produto['preco'] > 50:
        produto['e_caro'] = True #adiciono a chave e_caro para valores acima de 50 dentro do meu dicionario
        return True

nova_lista2 = filter(filtra, produtos)
print("\n usando a função")
for produto in nova_lista2:
    print(produto)



def filtra_idade(pessoas):
    if pessoas['idade'] >= 18 :
        pessoas['maior'] = True
        return True
    else:
        return False

lista_menores = filter(filtra_idade, pessoas)

print("\n todos os maiores de idade")
for menores in lista_menores:
    print(menores)