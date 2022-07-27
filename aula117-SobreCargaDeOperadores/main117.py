""""
No python, o comportamento dos operadores é definido por metodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuario.

"""
"""
Se eu faço assim o python nao consegue interpretar o que ele deve somar
"""
# class Retangulo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#

# r1 = Retangulo(10, 20)
# r2 = Retangulo(10, 20)
#
# print(r1 + r2)

"""
Ai eu faço dessa maneira
"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y


    """
    faço isso para que meu printo mostre o resultado da soma do meu retangulo
    """
    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y}) '>"

    """
    self representa a instancia e o other represemta o objeto
    """
    def __add__(self, other):
        """
        falo para o python que meu novo x é(x + x) e meu novo y é (y + y) que no casso é o self + o other
        """
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False



r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 =  r1 + r2
print(r1 == r2)
