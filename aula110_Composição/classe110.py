"""
Composição
relação mais forte entre classes, uma classe vai ser dona de objetos de outra classe
e se a classe principal for apagada, todos os objetos que a classe principal utilizou
serao apagados com ela.
"""


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ederecos = []

    def insere_endereco(self, cidade, estado):
        # chamo a classe Endereco e aqui eu faço a composição
        self.ederecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.ederecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        #assim que eu apago meu cliente da memoria e assim todos os endereços relacionado a ele
        print(f"{self.nome} Foi apagado")


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f"{self.cidade}/ {self.estado} foi apagado")
