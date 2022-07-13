import re


def remover_caracteres(cnpj):
    cnpj_limpo = re.sub(r'[^0-9]' , '' , cnpj)  # tudo que for diferente de 0-9 vai ser substituito para ''
    return cnpj_limpo

def remover_dois_digitos(cnpj):
    doze_digitos = cnpj[:-2]
    return doze_digitos


def verificar_primeiro_digito(cnpj):
    formula1 = [5 , 4 , 3 , 2 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2]
    multiplica = list(map(lambda x , y: x * y ,cnpj , formula1))
    multiplica = sum(multiplica)
    resultado = 11 - (multiplica % 11)

    if resultado > 9:
        resultado = 0
        return resultado
    else:
        return resultado


def verificar_segundo_digito(cnpj):
    formula2 = [6 , 5 , 4 , 3 , 2 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2]
    multiplica = list(map(lambda x , y: x * y , cnpj , formula2))
    multiplica = sum(multiplica)
    resultado = 11 - (multiplica % 11)
    if resultado > 9:
        return 0
    else:
        return  resultado
