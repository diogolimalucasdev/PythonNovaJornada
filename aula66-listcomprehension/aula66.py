l1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

l2 = [variavel for variavel in l1]  # quero que ele jogue cada valor do l1 em l2
print(l2)

exemplo2 = [v * 2 for v in l1]  # multiplicco cada elemento da miha lista por 2
print(exemplo2)

l2 = ['Luiz' , 'Mauro' , 'Maria']
exemplo4 = [v.replace('a' , '@').upper() for v in l2]  # para cada valor de v que comece com aletra a troque para @
print(exemplo4)

tupla = (
        ('chave' , 'valor') ,
        ('chave2' , 'valor2')
)
exemplo5 = [(y , x) for x , y in tupla]  # inverto os valores de chave e valor da tupla
print(exemplo5)
exemplo5 = dict(exemplo5)  # transformei a tupla em dicionario
print(exemplo5)

# suponha que eu queira filtrar uma lista

l3 = list(range(100))

# vou filtar todos os numeros dividos do por 2
exemplo6 = [v for v in l3 if v % 2 == 0]
print(exemplo6)

# vou filtrar todos os numeros dividos por 3 e por 8
exemplo7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(exemplo7)

# usando o else agora e fazendo a verificação primeiro
#verifico os numeros que sao possiveis dividir por 3 por 8 e os quais nao sao eu coloco 'nao é'
exemplo8 = [v if v % 3 == 0 and v % 8 == 0  else 'nao é' for v in l3]
print(exemplo8)
