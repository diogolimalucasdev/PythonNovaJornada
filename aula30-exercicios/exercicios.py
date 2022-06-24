"""
Faça um programa que pela ao usuario para digitar um numero inteiro, informe se este numero é par
ou impar. Caso i usuario nao digite um numero inteiro, informe que nao é um numero itneiro
"""

numero = input("digite um numero: ")
if numero.isnumeric():
    if int(numero) % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é Impar")
else:
    print("Nao é um numero inteiro")

"""
faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudação apropriada.
Ex. bom dia 0 -11, boa tarde 12- 17 e boa noite 18-23
"""

horas = input("Digite a hora: ")
minutos = input("Digite os minutos: ")

hora_certa = horas + minutos
hora_certa = int(hora_certa)

print(hora_certa)

if 0000 <= hora_certa <= 1100:
    print("Bom dia")
elif 1200 <= hora_certa <= 1700:
    print("Boa tarde")
else:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuario.se o nome tiver 4 letras ou menos escreva
"seu nome é curto"; se tiver entre 5 e 6 letras, ecsreva "seu nome é normal"; maior escreva "seu nome
é muito grande"
"""

nome = input("digite seu nome: ")
print(len(nome))
if len(nome) <= 4:
    print("seu nome é curto")
elif 4 < len(nome) <= 6:
    print("seu nome é normal")
else:
    print("seu nome é muito grande")
