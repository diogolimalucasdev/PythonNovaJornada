carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 3', 50))


v = 0

 # v é minha variavel onde sera armazenado o valor de v que esta dentro do for
 # c é rewponsavel por pegar o nome do produto podemos dizer assim, e v o valor do produto
 # e so armazeno em v o valor do produto
valor_total = [v  for c, v in carrinho] # meu jeito de fazer
print(sum(valor_total))

valor_total = sum([float(v)  for c, v in carrinho]) #jeito do professor
print(valor_total)