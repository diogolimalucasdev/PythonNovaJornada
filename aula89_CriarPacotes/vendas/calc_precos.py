from aula89_CriarPacotes.vendas.formata import preco


def aumento(valor , porcentagem , formata = False):
    r = valor + (valor * (porcentagem / 100))

    if formata:
        return preco.real(r)
    else:
        return r


def reducao(valor , porcentagem , formata = False):
    r = valor - (valor * (porcentagem / 100))

    if formata:
        return preco.real(r)
    else:
        return r
