"""
https://rszalski.github.io/magicmethods/
"""
"""
sao metodos que começam e terminam com dois underlines
"""

class A:
    "metodo que junto com o init pode constrtuir a classe, o new é chamado antes do init"
    def __new__(cls, *args, **kwargs):

        "se quiser que minha classe seja instanciada apenas uma vez eu faço o seguinte: "
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return cls._jaexiste

    "ele é chamado assim que minha classe é instanciada, esse é um dos metodos magicos"
    def __init__(self):
        print('EU SOU O INIT')

a = A()
b= A()
c = A()

"como eu nao permitir criar duas instancia da minha classe, tudo que instanciar minha classe vai ser uma copia"
print(a == c)
print(c == b)

"podemos ver que todos tem o mesmo id"
print(id(a), id(b), id(c))