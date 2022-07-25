"AO inves de eu fazer assim"
# class CLiente:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
# class Aluno:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

"A herança funciona como uma hierarquia, de baixo para cima, a cada subclasse tem mais definições," \
"como no meu aluno ele herdou tudo de pessoa e teve suas definições assim como o cliente"



"eu crio minha classe assim!"
"essa é chamada de super classe"
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print('falando')
        print(f'{self.nomeclasse} que chamou e esta falando')


"Aqui eu falo que aluno e cliente herdam de pessoa, que aluno e cliente é uma pessoa"
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando ')


"essas sao chamadas de subclasse"
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando ')
