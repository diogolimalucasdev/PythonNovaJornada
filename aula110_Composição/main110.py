from classe110 import  Cliente

cliente1 = Cliente('Diogo', 21)
cliente1.insere_endereco('Itapecerica Da Serra', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
"apagando meu cliente 1 da memoria e seus endereços conseguentemente "
del cliente1
print()

cliente2 = Cliente('Miguel', 13)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('São Paulo', 'SP')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('Maria', 44)
cliente3.insere_endereco('Segipe', 'SE')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('####################################################################')

