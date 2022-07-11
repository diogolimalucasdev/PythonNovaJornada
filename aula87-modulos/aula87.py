#modulos padrão do python
#modulos sao arquivos .py (que contem codigo python) e servem para expandir as funcionalidade
#padrao da linguagem

#veja os modulos padrao do python em :
#https://docs.python.org/3/py-modindex.html


#qual plataforma o python esta seno rodadoe importando todo os modulo
# import sys
# # print(sys.platform)

#outra mandeira de importar o modulo

# from sys import platform #importo apenas o que eu quero usar
# print(platform)

#apelidando o modulo para como eu quero usar no meu codigo
# from sys import platform as so
# print(so)

#modulod e gerar numero "aleatorios"
import random
print(random.randint(0, 10))

#importo tudo de um modulo
from random import *  #o * serve para falar que quero importa tudo

#import mais de uma coisa
# from random import randint, random