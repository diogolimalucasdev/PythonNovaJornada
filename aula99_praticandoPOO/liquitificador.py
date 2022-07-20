class Liquitificador:

    def __init__(self , ligado = False , girando = False):
        self.ligado = ligado
        self.girando = girando

    def ligar(self):
        if self.ligado:
            print('O liquitificador ja esta Ligado')
            return
        print(f'Ligado ')
        self.ligado = True

    def girar(self , velocidade):
        if not self.ligado:
            print('Ligue o liquitificador!')
            return
        print(f'O liquitificador esta ligado na velocidade {velocidade}')

    def desligar(self):
        if not self.ligado:
            print('O liquitificador ja esta desligado.')
            return
        elif self.ligado:
            print('Desligar...')
            self.ligado = False
