class A:
    def __init__(self):
        pass

    "toda vez que eu configurar um atributo novo na minha classe esse metodo vai ser chamado"
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    "esse emtodo serve para toda vez que eu tentar dar print na minha instancia de classe"
    "e eu decido o que ele vai retornar"
    def __str__(self):
        return "<class 'A'"

    "agora eu mudo o que eu quero tambem utilizando o len"
    def __len__(self):
        return 21




a = A()
print(a)
print(len(a))
a.nome = 'Diogo Lima'
a.idade = 21

print(a.nome, a.idade)
