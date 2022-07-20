# Setter = congifurando um valor (=) escrevo
# Getter = obter um valor (.) ler  => print

class Pessoa:
    def __init__(self, nome):
        # eu tenho que ocultar essee atributo pois eu to utilizando getter e setter
        # pra isso eu utilizo o _ para "esconder" o meu nome
        self._nome = nome
        #
        # quando eu chamo minha classe em p1 =Pessoa() e depois print(p1.nome) ele executa primeiro meu init
        # se eu quiser mudar isso eu chamo meu metodo setter no meu init
        # self.nome = nome
        #

        # isso manda pro python que minha função é um nome pro python

    @property
    def nome(self):
        return self._nome
    # para criar um setter em python eu tenho que pegar um nome de um nome que eu coloquei o
    # ... @property e colocar o nome dele.setter
    @nome.setter
    def nome(self, nome):
        self._nome = nome

p1 = Pessoa('Maria')
# quando eu tenho um property eu passo pro python que meu metodo é um atributo por isso nao preciso passar o () em nome
print(p1.nome)

# agora eu passo para o meu setter que o valor do atributo nome sera 'Diogo'
p1.nome = 'Diogo '

# depois de ja ter passado o valor pro atributo eu vou e peço para ver o meu atributo usando o getter
# podemos ver como o valor foi modificado
print(p1.nome)
