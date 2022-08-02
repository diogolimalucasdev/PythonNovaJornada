from enum import Enum


class Direction(Enum):
    right = 0
    left = 1
    up = 2
    down = 3


#
# def move(direction):
#     if direction != 'right' and direction != 'left':
#         raise ValueError('Cannot move in this direction')
#     return f'Moving {direction}'


# if __name__ == '__main__':
# #     print(move('right'))
# #     print(move('left'))
# #     print(move('up'))
# #     print(move('down'))

def move(direction):
    # verifico se a direção que estou recebendo vem da minha classe Direction, se nao vir eu apresento um erro
    if not isinstance(direction, Direction):
        raise ValueError('Cannot move in this direction')
    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Direction.right))
    print(move(Direction.left))
