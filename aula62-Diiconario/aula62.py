d1 = {'chave1': 'valor1'}
d1['nova chave'] = 'Valor da nova chave'

print(d1)

print(d1['chave1'])

d2 = {
        'str': 'valor' ,
        123: 'Outro valor' ,
        (12 , 34 , 5): 'Tupla'

}

print(d2[12 , 34 , 5])  # acessando a chave que esta contida por um tupla

# outra mandeira de buscar a chave
d2['nomedachave'] = 'Agora ela existe'
if d2.get('nomedachave') is not None:
    print(d2.get('nomedachave'))
else:
    print("nao existe")
