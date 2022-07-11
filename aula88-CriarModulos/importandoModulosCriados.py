import modulos  # importando tudo que esta no meu outro arquivo py

# se for executado aqui, ele nao executa os print como nos modulos

# agora eu posso usar meu modulo tranquilo
print(modulos.PI)

lista = [5 , 6 , 7 , 8 , 9 , 10]

print(modulos.dobrar_lista(lista))

# agora realizando de outra maneira os imports

from modulos import dobrar_lista, multiplica  # aqui eu importo oq eu quiser do meu modulo
from outro_modulo import fala_oi

lista_nova = [11 , 22 , 33 , 44 , 55 , 66 , 77 , 88 , 99]
print(dobrar_lista(lista_nova))
print(multiplica(lista_nova))

fala_oi()
