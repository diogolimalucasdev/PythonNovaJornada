# exemplo de agregação é uma classe carro e uma clsse roda, uma precisa da outra para funcionar

#essa classe pode existir sozina mas para funcionar precisa da classe produto
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

#ja esta classe pode existir sozinha sem precisa do carrinho de compras
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
