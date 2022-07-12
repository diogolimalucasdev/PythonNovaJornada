

#com a função asssim toda vez que eu chamasse a função, ele ia atribuir o valor da lista anterior a
#minha nova lista

# def lista_de_clientes(clientes_iteravel , lista = []):
#     lista.extend(clientes_iteravel)
#     return lista

#por isso eu faço a função assim, dessa maneira cada lista vai ser independente
def lista_de_clientes(clientes_iteravel , lista =None):
    if lista is None: # se a litsa for None eu crio uma lista em branco
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_clientes(['joao' , 'maria' , 'eduardo'])
clientes2 = lista_de_clientes(['marcos' , 'jonas' , 'zico'])

print(clientes1)
print(clientes2)
