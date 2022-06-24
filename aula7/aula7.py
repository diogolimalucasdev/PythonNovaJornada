nome = 'diogo lima'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

"formas de formartar seu texto"
print(nome , 'tem' , idade , 'anos de idade e seu imc é' , imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # arredondado o numero
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n = nome, i = idade, im = imc))  # passando como parametros
