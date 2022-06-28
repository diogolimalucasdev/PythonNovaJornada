# lista, tuples, str -> sequencia de dados -> Iteravel
nome = 'Diogo Lima'

for letra in nome:
    print(letra)

# o for transforma minha variavel "nome" em interador para conseguir dar o next

#criando minha variavel em interador na mao
iterador = iter(nome)
print(next(iterador)) #me retorna a primeira letra do meu nome, esse é o papel do for


######################################
