texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

nome = 'aumentar todos t e a'
novo_nome = ''

for letra2 in nome:
    if letra2 == 'a':
        novo_nome += letra2.upper()
    elif letra2 == 't':
        novo_nome += letra2.upper()
    else:

        novo_nome += letra2
print(novo_nome)