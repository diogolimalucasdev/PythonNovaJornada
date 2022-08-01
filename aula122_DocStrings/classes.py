"""
Descrição rápida e simples

Este modulo é apenas um teste para vermos como funciona o help utilizando a docstrings,
onde eu estou estudando python para um dia se tornar programador profissional que é o meu maior sonho no momento
e no futuro conseguir comprar um apartamento para meus pais e conseguir comprar o meu para construi uma familia, e
tambem ajudar meus irmaos.Hoje é dia 01/08/2022 e eu estou atras do meu sonho, hj é um dia em que estou bem triste
pois a ansiedade e a depressao esta acabando comigo pois nao estou conseguindo continuar minha vida e ir atras dos meus
sonhos.

"""


class MinhaClasse:
    """Documentação Nomrmal

    conforme qualquer outra documentação que vopce tenha usado anteriormente

    """

    atributo_1 = 1
    atributo_2 = 'Valor'

    def __init__(self, texto):
        """Incializa os dados

        :param texto: o texto da classe
        :type texto: str

        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
            """Meétodo que exibe um texto de 100 caracteres na tela

            :paramtexto: texto: Um texto de 100 caracteres
            :type: str

            :raises ValueError: Se o texto tiver mais que 100 caracteres
            :raise TypeError: Se o texto nao for uma string

            """

            if not isinstance(texto, str):
                raise TypeError('texto precisa ser uma string')

            if len(texto) > 100:
                raise ValueError('Texto precisa ter 100 caracteres ou menos')

            return texto


a = MinhaClasse('testando texto')
print(a.texto)
