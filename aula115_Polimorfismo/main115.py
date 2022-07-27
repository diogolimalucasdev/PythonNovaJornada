"""
Polimorfismo é o principio que permite que classes derivadas de uma mesm superclasse tenham
métodos iguais(da mesma assinatura) mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""

"""
Usei polimorfismo na aula 114
"""

from abc import ABC, abstractmethod

"super classe"
class A(ABC):

    @abstractmethod
    def fala(self, msg): pass


class B(A):
    "mesmo metodo na classe B e C mas como comportamento diferente"
    def fala(self, msg):
        print(f'B esta falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C esta falando {msg}')

b= B()
c = C()
b.fala("Um Assunto")
c.fala("Outro Assunto")