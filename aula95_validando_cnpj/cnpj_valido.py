"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
from cnpj import remover_caracteres , verificar_primeiro_digito , verificar_segundo_digito, remover_dois_digitos

cpnj = input('Digite o cnpj: ')
cnpj_limpo = remover_caracteres(cpnj)

cnpj_sem_caracter = remover_dois_digitos(cnpj_limpo)
# print(f"Cnpj sem os dois digitos: {cnpj_sem_caracter}")

cnpj_sem_caracter = list(cnpj_sem_caracter)
# print(cnpj_sem_caracter)

cnpj_sem_caracter = [int(val) for val in cnpj_sem_caracter]
# print(f"cnpj em loista sem os dfois digitios {cnpj_sem_caracter}")

primeiro_digito = verificar_primeiro_digito(cnpj_sem_caracter)
# print(f"primeiro digito retorno {primeiro_digito}")

cnpj_sem_caracter.append(primeiro_digito)
# print(f"cnpj com um caracter ja: {cnpj_sem_caracter}")
# print(f"o que ta chegando do primeiro digito {primeiro_digito}" )
segundo_digito = verificar_segundo_digito(cnpj_sem_caracter)
# print(f"o que ta chegando do segundo digito {segundo_digito}")

cnpj_sem_caracter.append(segundo_digito)
# print(f"cnpj com dois caracteres ja: {cnpj_sem_caracter}")

cnpj_limpo = list(cnpj_limpo)
cnpj_limpo= [int(val) for val in cnpj_sem_caracter]

if cnpj_limpo == cnpj_sem_caracter:
    print("Cnpj é valido!")
else:
    print("Cnpj nao é valido")







