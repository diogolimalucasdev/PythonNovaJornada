import csv

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

"criando um arquivo apartir do meu csv original"
with open('clientes2.csv', 'w+') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter= ',',
        quotechar = '"',
        quoting=csv.QUOTE_ALL
    )

    "pegando as chaves desse csv"

    chaves = dados[0].keys()
    chaves = list(chaves)

    "escrevendo as chaves"
    escreve.writerow(
            [
                chaves[0],
                chaves[1],
                chaves[2],
                chaves[3],

            ]
    )


    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],

            ]
        )