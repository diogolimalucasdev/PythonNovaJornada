"""
classes abstratas sao classes genericas que eu nao quero que ela seja instanciadas ou seja chamada,
crio tambem um metodo abstract onde as classes filhas terao que chamar esse metodo
"""
"""
importo o modulo abstract base classe(abc) e o decorador abstractmethod
"""
from abc import ABC, abstractmethod

class A(ABC):

    "agora eu crio meu metodo"
    @abstractmethod
    def falar(self):
        pass

"assim eu obrigo que minha classe filha tenha o metodo abstrato falar"
class B(A):
    "se eu comentar esse metodo ele vai me apresentar um erro"
    def falar(self):
        print('Falando....Classe B....')


a = B()
a.falar()

"nao posso chamar minha classe A tambem "
# classeA = A()
