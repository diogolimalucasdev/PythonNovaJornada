"""
Associação -Usa | Agregação - Tem | Composição - É dono | Herança - É

"""
from claases111 import *

cliente1 = Cliente('Diogo Lima', 21)
print(cliente1.nome)
cliente1.falar()

"metodo da minha subclasse cliente"
cliente1.comprar()

aluno1 = Aluno('Miguel Lima', 13)
print(aluno1.nome)

"metodo da minha subclasse aluno"
aluno1.estudar()


"entendendo a herança se eu criar uma pessoa chamanda direto minha superclasse eu vou ter apenas" \
"as definições gerais "
pessoa1 = Pessoa('Maria Lima', 44)

"como eu estanciei minha superclasse eu so tenho o metodo falar"
pessoa1.falar()