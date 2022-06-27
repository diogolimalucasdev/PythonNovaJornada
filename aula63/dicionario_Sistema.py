perguntas = {
        'Pergunta 1': {
                'pergunta': 'Quanto é 2+2 ?',
                'respostas': {
                        'a': '1',
                        'b': '3',
                        'c': '4',
                        'd': '5'
                },
                'resposta_certa': 'c',
        },
        'Pergunta 2': {
                'pergunta': 'Quantos é 3 x 2 ?',
                'respostas': {
                        'a': '12',
                        'b': '19',
                        'c': '2',
                        'd': '6'
                },
                'resposta_certa': 'd',
        }
}
respostas_certas = 0
#acesso primeiro os items do dicionario, ou seja chave da pergunta1 e seu valor e da pergunta 2 e seu valor
for chave_pergunta, valor_pergunta in perguntas.items():

    #aqui estou passando na primeira e segunda pergunta e pegando o valor da chave da pergunta(valor_pergunta)
    print(f'{chave_pergunta}: {valor_pergunta["pergunta"]}')

    print('Respostas: ')

    #aqui pego os item da chave respostas e separo em chave e valor
    for chave_resposta, valor_resposta in valor_pergunta["respostas"].items():
        print(f'{chave_resposta} = {valor_resposta}')

    resposta_usuario = input("Sua resposta: ")
    if resposta_usuario == valor_pergunta["resposta_certa"]:
        print("Acertou")
        respostas_certas += 1
    else:
        print("Errou")

    print()




perguntas2 = {
        'pergunta1': {
                'pergunta': 'Qual a capital do Brasil',
                'resposta': {
                        'a': 'Brasilia',
                        'b': 'São Paulo',
                        'c': 'Rio de Janeiro',
                        'd': 'Amazonas'
                },
                'resposta_certa': 'a'
        },
        'pergunta2':{
                'pergunta': 'Qual o maior time do Brasil',
                'resposta': {
                        'a': 'São Paulo',
                        'b': 'Palmeiras',
                        'c': 'Corinthians',
                        'd': 'Flamengo',
                },
                'resposta_certa': 'c',
        }

}


for chave_pergunta2, valor_pergunta2 in perguntas2.items():
    print(f'{chave_pergunta2} : {valor_pergunta2["pergunta"]}')

    print("respostas: ")
    for chave_resposta2, valor_resposta2 in valor_pergunta2["resposta"].items():
        print(f'{chave_resposta2} = {valor_resposta2}')

    print()
    resposta_usuario = input("Sua resposta: ")
    if resposta_usuario == valor_pergunta2["resposta_certa"]:
        print("Acertou")
        respostas_certas += 1
    else:
        print("Errou")

qtd_perguntas = len(perguntas) + len(perguntas2)
porc_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou: {respostas_certas}')
print(f'A porcentagem foi de {porc_acerto:.2f} %')