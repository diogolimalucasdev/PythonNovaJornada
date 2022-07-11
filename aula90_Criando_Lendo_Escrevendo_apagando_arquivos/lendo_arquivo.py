# https://docs.python.org/3/library/functions.html#open

# modo mais basico
file = open('abc.txt' , 'w+')  # abro um arquivo, no momento eu nao tenho ele(o python vai criar), e quero leitura e
# escrita(w+)

# estrou escrevendo nele
file.write('Linha 1 \n')  # e escrevo no meu arquivo
file.write('Linha 2 \n')
file.write('Linha 3 \n')

# primeiro jeito de ler meu arquivo
# mando meu cursor par as primeiras linhas para que eu possa ler do meu arquivo
file.seek(0 , 0)
print(file.read())

# segunda maneira - lendo linha por linha
print('2 maneira ########################')
file.seek(0 , 0)
print(file.readline() , end = '')  # end para nao pegar a quebra de linha, readline pega linha por linha
print(file.readline() , end = '')
print(file.readline() , end = '')

# terceira maneira
print("\n 3 maneira ################")
file.seek(0 , 0)  # seto meu crusor novamente
for linha in file.readlines():  # readlines gera uma lista por isso vou ursar o for para pecorrer
    print(linha, end="")  # printo linha por linha

# fecho meu arquivo quando eu termino de utilizar ele
file.close()
