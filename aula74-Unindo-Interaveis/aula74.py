"""
Zip - Unindo itervaies        # nao precisa importar nada paea utilizar
Zip_longest - Itertools
"""
from itertools import zip_longest, count

# codigo
indice = count()
cidades = ['São Paulo' , 'Belo Horizonte' , 'Salavador' , 'Monte Belo']

# codigo....
estados = ['SP' , 'MG' , 'BA']  # eu quero unir essas duas listas, sao paulo > sp...

# o zip junto as duas lista e vai preencher o que estiver faltando com none
cidades_estados = zip(
        indice,
        estados ,
        cidades,)

print(list(cidades_estados)) #ele preencheu com 'Estado' onde estava faltando

for valor in cidades_estados:
    print(valor)

#desempacotando
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)


#####################################################################################



# codigo
cidades = ['São Paulo' , 'Belo Horizonte' , 'Salavador' , 'Monte Belo']

# codigo....
estados = ['SP' , 'MG' , 'BA']  # eu quero unir essas duas listas, sao paulo > sp...

cidades_estados = zip(estados , cidades)  # o zip junto as duas lista ate terminar a lista menor

# for valor in cidades_estados:
     # print(valor[0] , valor[1])
    # # ou assim
    # print(valor)


