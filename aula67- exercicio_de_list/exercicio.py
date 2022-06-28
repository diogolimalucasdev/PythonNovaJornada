string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10

lista_nova = [string[i:i + n] for i in range(0, len(string) , n)]
# finalizado = str(lista_nova).replace(',', '.').replace(' ', '')
finalizado = '.'.join(lista_nova)
print(lista_nova)
print(finalizado)

