from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # como se fosse uma função normal, mas dentro da minha classe, nao recebe nem cls(minha classe) nem self(estancia)
    # nao posso usar o self nem cls aqui dentro
    @staticmethod
    def gerar_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Diogo', 21)
p1.get_ano_nascimento()

# posso chamar o metodo estatico assim
print(Pessoa.gerar_id())

# ou assim, mas relembrando que eu nao tenho acesso ao meu metodo, mas posso chamalo
print(p1.gerar_id())
