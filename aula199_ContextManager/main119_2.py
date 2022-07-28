"""
outra maneira de criar gerenciador de contexto"
"""

from contextlib import contextmanager

"eu tenho que usar o decorador para transformar minha função em um contextmanager"
@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print('Abrindo arquivo')
        yield arquivo
    finally:
        print('Fechando Arquivo')
        arquivo.close()

with abrir('def.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
