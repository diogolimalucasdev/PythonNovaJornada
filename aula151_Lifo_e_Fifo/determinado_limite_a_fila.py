"ja na fila o primeiro a entrar é o primeiro a sair, first in, first out "
from collections import deque
from time import sleep

"to determinando o valor maximo da minha fila, como minha fila tem valor maximo de 5, quando eu ultrapasso" \
"esse valor, o primeiro valor é removido"
fila = deque(maxlen=5)
fila.append('Diogo Lima')
fila.append('Maria')
fila.append('Luiz Otavio')
fila.append('Marcos')
fila.append('Laryssa')
print(fila)
fila.append('Miguel')
print("O primeiro valor foi removido")

print(fila)


tempo = deque(maxlen=10)

for i in range(1000):
    tempo.append(i)
    sleep(1)
    print(tempo)