""""
Pilhas e filas
Pilha(stack) - Lifo - last in, first out.
    Exemplo> Pilha de livros que sao adicionados um sobro o outro
Fila(queue) - FIFO- first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os indices serão modificados
"""

livros = list()
livros.append('Livro 1') #1
livros.append('Livro 2') #2
livros.append('Livro 3') #3
livros.append('Livro 4') #4
livros.append('Livro 5') #5
'ultimo item da minha lsta que é o primeiro da miha pilha por isso last in, first out'
livro_removido = livros.pop() #5
livro_removido = livros.pop() #4
livro_removido = livros.pop() #3
livro_removido = livros.pop() #2
livro_removido = livros.pop() #1


"ja na fila o primeiro a entrar é o primeiro a sair, first in, first out "
from collections import deque

fila = deque() #um elemento deque que é uma lista normal
fila.append('Diogo Lima')
fila.append('Maria')
fila.append('Luiz Otavio')
fila.append('Marcos')
print(fila)
print(f'Saiu: {fila.popleft()}') #removo o Diogo Lima pois ele foi o primeiro da lista
print(f'Saiu: {fila.popleft()}') #saiu maria
print(f'Saiu: {fila.popleft()}') #saiu luiz otavio
print(f'Saiu: {fila.popleft()}') #saiu marcos
print(fila)

# for nome in fila:
#     print(nome)


"inserindo um valor em um indece determinado por mim"
minha_lista = deque(maxlen=10)
minha_lista.extend([1,2,3,4,5,6])
print(minha_lista)
minha_lista.insert(2, 'Estou inserindo no indice 2, no lugar do 3')
print(minha_lista)
