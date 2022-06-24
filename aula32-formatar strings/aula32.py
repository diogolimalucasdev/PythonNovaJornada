"""
formatando valores com modificadores
:s - TEXTo(strings) :s
:d - INTEIROS (int) :d
:f - NUMEROS DE PONTO FLUTUANTE (float) :f
:.(Numero)f - QUnatidade de casas deicimais (float) :.2f
:(CARACTERE) ( > ou < ou ^)(QUANTIDADE) (TIPÒ - s, d ou f)

> - ESQUERDA
< - DIREITA
^ - CENTRO



"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao))  # quero apenas 2 casas decimas e F siginifica ponto flutuante
print(f'{divisao:.2f}')

num_3 = 1
print(f'{num_3:0>10}')  # to falando que quero que seja prenchicado 10(contado com o 1) casas e que seja preenchido
# por 0 a esquerda

num_4 = 1150
print(f'{num_4:2>10}')  # agora estou preenchendo com 2 mas para o lado direito

num_5 = 2222
print(f'{num_5:a^10}')  # posso adicionar letra

num_6 = 33
print(f'{num_6:.2f}')  # tranformando para float

num_7 = 44
print(f'{num_7:0<7.2f}')  # agora alem de tranformar para float eu adiciona mais zeros

nome = 'Diogo Lima Lucas'
print(f'{nome:#^50}')  # centralizando meu nome ao centro e adicionado # aos lados

nome = 'DIOGO LIMA LUCAS'
print(f'{nome:s}')
