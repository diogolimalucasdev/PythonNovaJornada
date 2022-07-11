# https://docs.python.org/3/library/functions.html#open

#com o w+ eu apago tudo o que tenho no arquivo e crio um novo
with open('novo_arquivo.txt', 'w+') as file:
    file.write('Arquivo em branco\n')
    file.write('Linha4 Nova\n')
    file.write('Linha5\n')
    file.write('Linha6\n')

    file.seek(0)
    print(file.read())