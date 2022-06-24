def funcao(arg , arg2):
    return arg * arg2


var = funcao(2 , 2)

a = lambda x , y: x * y  # posso usar isso quando quiser passa uma função de parametro para outra função
print(a(2 , 2))

# exemplo

lista = [  # vamos imaginar uma lista de produtos e seus preços
        ['P1' , 13] ,
        ['P2' , 6] ,
        ['P3' , 6] ,
        ['P4' , 50] ,
        ['P5' , 68]
]


def func(item):
    return item[1]


lista.sort(key = func)  # estou ordenando a lista pelo preço, por isso faço a função para pegar o item de preço da lista
print(lista)

# inverter a lista agora
lista.sort(key = func , reverse = True)
print(lista)

# agora utilizando a lambda para realizar isso tudo

lista.sort(key = lambda item: item[1])
print(lista)

# outro modo

print(sorted(lista , key = lambda i: i[0]))
