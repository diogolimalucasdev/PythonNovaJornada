"""
O que são dataclasses? o modulo dataclasses fornece um decorador e funções para criar automaticamente metodos, como
__init__(), __repr__(), __eq__() etc... em classes definidas pelo usuario
Basicamente, dataclasses sao syntax sugar para criar classes normais.Foi orginalmente descrito na PEP 557.
Adicionado na versao 3.7 do python
Documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

# como criar classes usando o dataclass

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: 'str'

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Diogo', 'Lima')
print(p1)
print(p1.nome_completo())