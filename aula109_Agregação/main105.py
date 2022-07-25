from classes105 import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto1 = Produto('Camiseta', 20.99)
produto2 = Produto('Iphone', 5000)
produto3 = Produto('Caneca', 15)

#inserindo produto na minha classe utilizando a classe produto
carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)
carrinho.inserir_produto(produto1)

# vejo se foi adicionado mesmo
carrinho.lista_produto()

#ver a soma total do carrinho
print(carrinho.soma_total())

