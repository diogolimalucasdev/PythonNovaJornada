import re

REGRESSIVOS = [6 , 5 , 4 , 3 , 2 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2]


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    if eh_sequencia(cnpj):
        print("É uma sequencia")
        return False

    novo_cnpj = calcula_digito(cnpj = cnpj , digito = 1)
    novo_cnpj = calcula_digito(cnpj = novo_cnpj , digito = 2)

    if novo_cnpj == cnpj:
        return True
    else:
        return False

    print(cnpj)


def calcula_digito(cnpj , digito):
    if digito == 1:  # se for meu primeiro digito que eu quero dewcobrir
        regressivos = REGRESSIVOS[1:]  # minha lista de regressivo vai começar apartir do 2 numero da lista
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos): #utilizo o enumarate para pegar os valores de regressivo
       total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)  # verificio se meu cnpj é uma sequencia de mesmos numeros

    if sequencia == cnpj:
        return True
    else:
        return False


def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]' , '' , cnpj)
