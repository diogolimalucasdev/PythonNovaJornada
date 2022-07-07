# https://docs.python.org/3/library/exceptions.html

# como lançar as proprias exceções
def divide(n1 , n2):
    if n2 == 0:
        raise ValueError("N2 nao pode ser 0")  # estou criando minha propria exceção
    return n1 / n2


try:  # captruar minha exceção
    print(divide(2 , 0))
except ValueError as error:  # assim busco o valor do erro
    print('Voce esta tentando dividr por 0')
    # print(error)

#
# def divide(n1 , n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('log: ', error)
#         raise
#
# try:
#     print(divide(2 , 0))
# except ZeroDivisionError as error:
#     print(error)
