""" Documentação deste modulo
Ele nao faz nada, mas é so um exemplo pra voce
Typing - https://docs.python.org/3/library/typing.html
"""
# podemos ver codigos onde o desenvolvedor quais sao os tipos da minha variavel
x: int = 10
y: float = 10.5
z: bool = False
a: str = 'valor'


# quando eu colco uma setinha depois da minha função eu indico qual vai ser o tipo do meu return
def funcao(p1: float, p2: str, p3: dict) -> float:
    return 10.10


# dessa maneira o pycharm vai te indicar o tipo certo do parametro
print(funcao(2.2, 'valor', {}))
