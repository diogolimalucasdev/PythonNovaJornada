import math

PI = math.pi

def dobrar_lista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

lista= [1,2,3,4,5]

if __name__ == '__main__': # se o arquivo for executado diretamente aqui, ele executa os print
    print(dobrar_lista(lista))
    print(multiplica(lista))
    print(PI)

    print(__name__)

