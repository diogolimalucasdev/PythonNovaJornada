"""
Descrição rápida e simples

Este modulo é apenas um teste para vermos como funciona o help utilizando a docstrings,
onde eu estou estudando python para um dia se tornar programador profissional que é o meu maior sonho no momento
e no futuro conseguir comprar um apartamento para meus pais e conseguir comprar o meu para construi uma familia, e
tambem ajudar meus irmaos.Hoje é dia 01/08/2022 e eu estou atras do meu sonho, hj é um dia em que estou bem triste
pois a ansiedade e a depressao esta acabando comigo pois nao estou conseguindo continuar minha vida e ir atras dos meus
sonhos.

"""

variavel_1 = 'valor 1'

#a primeira linha da minha função deve ser minha documentação
def foma(x, y):
    """soma x e y """
    return x + y

def multiplica(x, y, z=None):
    """Multiplica x, y, z

        Multiplica x, y e oz, O programador por omitir a variavel z caso nao tenha necessidade de usa-la
    """
    print(z)
    if z:
        return x * y
    else:
        return x * y * z

variavel_2 = 'valor 2'
variavel_3 = 'valor 3'
variavel_4 = 'valor 4'
