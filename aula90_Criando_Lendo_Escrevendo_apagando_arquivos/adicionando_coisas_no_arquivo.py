# https://docs.python.org/3/library/functions.html#open

#o poe o cursor no final, entao tudo oq ue eu escrever vai ser escrito no final
with open('novo_arquivo.txt', 'a+') as file:
    file.write('Adicionando linha\n')
    file.write('Linha4 Nova\n')
    file.write('Linha5\n')
    file.write('Linha6\n')

    file.seek(0)
    print(file.read())