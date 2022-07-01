"""
count - iterador
"""
from itertools import count

contador = count(start=5, step=2) #start inicio, setp de quanto em quantos
contador_invertido = count(start=5, step=-2) #start inicio, setp de quanto em quantos, estou andando para tras

for valor in contador:
    print(round(valor, 2)) #round , quantas casas decimais eu quero
