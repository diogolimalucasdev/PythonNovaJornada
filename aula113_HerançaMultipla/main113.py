"""
Site onde eu entendi sobre
https://www.alura.com.br/apostila-python-orientacao-a-objetos/
heranca-multipla-e-interfaces#:~:text=Problema%20do%20diamante&text=No%20Python%2C
%20%C3%A9%20poss%C3%ADvel%20que,das%20classes%20B%20e%20C%20.
"""


class A:
    def falar(self):
        print('Falando... Estou na Classe A')


"estou herdando minha classe A"
class B(A):
    "estou sobescrevendo o metodo falar da classe A"
    def falar(self):
        print('Falando.....Estou na Classe B')


class C(A):
    "estou sobescrevendo o metodo falar da classe A"
    def falar(self):
        print('Falando.....Estou na Classe C')


"Herança multipla, o python vai buscar pelo primeiro parametro no meu caso é a class B"
class D(B, C):
    pass


d = D()
d.falar()
