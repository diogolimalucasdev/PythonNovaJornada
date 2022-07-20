class Pessoa:
    ano_atual = 2022

    def __init__(self , nome , idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # metodo de classe, e ao inves de usar o self eu uso cls, pois o self eu referencio uma instancia
    # cls eu to referenciando a classe e nao uma estancia por isso nao uso o self
    @classmethod
    def por_ano_nascimento(cls , nome , ano_nascimento):
        # posso criar uma variavel aqui sem o self, mas vai ficar disponivel somente aqui
        # quandp eu tenho o cls eu tenho acesso a atributos da minha classe como o ano_atual
        idade = cls.ano_atual - ano_nascimento

        # estou retornando a propria classe, por isso abro o cls(), com os parametros nome e idade
        return cls(nome , idade)


p1 = Pessoa('Diogo' , 21)
p1.get_ano_nascimento()

# Usando o  metodo de classe, criando a pessoa
p2 = Pessoa.por_ano_nascimento('Diogo' , 2001)

# nome do modulo
print(p2)

print(p2.nome , p2.idade)
