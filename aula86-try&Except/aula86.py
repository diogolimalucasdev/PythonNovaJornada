def converte_numero(valor):
    try:
        valor = int(valor) #tenta tranformar isso para inteiro
        return valor
    except ValueError as erro:
        try:
            valor = float(valor) #se nao funcionaro inteiro, tenta transformar para float
            return valor
        except ValueError:
            pass

while True:
    numero = converte_numero(input('Digite um numero: '))


    if numero is None:
        print('Isso nao é um numero!')
    else:
        print(numero * 5)

    # if numero is not None:
    #     print(numero * 5)
    # else:
    #     print('Isso nao é numero!')
