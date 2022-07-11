# primeira maneira
import vendas.calc_precos
preco = 49.90
# acesso a pasta vendas, dentro de vendas acesso ao arquivo calc_precos e dentro dele a função aumento
preco_com_aumento = vendas.calc_precos.aumento(valor = preco , porcentagem = 15)
print(round(preco_com_aumento , 2))

# segunda maneira
from aula89_CriarPacotes.vendas import calc_precos  # import o cal_precos completo
preco2 = 55.50
preco_com_aumento2 = calc_precos.aumento(valor = preco2 , porcentagem = 10 , formata=True)
print(preco_com_aumento2)

# terceira forma
from aula89_CriarPacotes.vendas.calc_precos import reducao
preco3 = 44.90
preco_com_reducao = reducao(valor = preco3 , porcentagem = 10, formata=True)
print(preco_com_reducao)


#importando meu pacote
from vendas.formata import preco
print(preco.real(20))

