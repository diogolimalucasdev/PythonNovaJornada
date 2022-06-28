import sys

lista = [0,1,2,3,4,5,6,7]

print(hasattr(lista, '__iter__')) #verificando se minha lista é interavel


num = 1234
print(hasattr(num, '__iter__')) #false pois a variavel nao é iteravel

#transformando uma lista em interador
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

l1 = [x for x  in range(10000)] #87616 bytes
l2 = (x for x  in range(10000)) #olha a diferença de bytes entre um e outro 112 bytes

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
