
# a diferença é que eu nao preciso mandar fechar o arquivo, ele ja fecha automaticamente ao final do codigo
with open('novo_arquivo.txt', 'w+') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)
    print(file.read())
