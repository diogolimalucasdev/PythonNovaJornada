from liquitificador import Liquitificador

liquitificador = Liquitificador()

liquitificador.ligar()
liquitificador.girar(10)
liquitificador.desligar()

#tentar desligar o liquitificador que ja se encontra desligado
liquitificador.desligar()

#irei ligar novamente e tentar ligar duas vezes
liquitificador.ligar()
liquitificador.ligar()

#irei desligar e veirficar se eu consigo determinar a velocidade
liquitificador.desligar()
liquitificador.girar(20)