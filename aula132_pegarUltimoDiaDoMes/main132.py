from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

"para pegar o ultimo dia do mes"
#eu pego a daa atual
data_atual = datetime.now()
#o mes atual
mes_atual = int(data_atual.strftime('%m'))
#e assim eu descubro qual o ultimo dia do meu mes
print(mes_atual, mdays[mes_atual])

"setar o local em qual estamos pelo local padrao do usuario atual do pc"
setlocale(LC_ALL, '')


dt = datetime.now()
formatcao = dt.strftime('%A, %d de %B de %Y')
print(formatcao)