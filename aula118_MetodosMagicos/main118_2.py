"mesmo conceito so que outro exemplo de metodos magicos"

class A:
    def __init__(self):
        pass
        # print("EU SOU O INIT ")

    "faz como que minha classe se comporte como uma função"
    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i
        return resultado, kwargs

    @staticmethod
    def falar_oi():
        print('fala oi')



a = A()
variavel = a(1,2,3,4,5, frase ='Diogo chamando a classe como se fosse uma função')
"fiz a multiplicação dos meus args e mostrei o meu kwargs"
print(variavel)

"eu posso trabalhar com a minha classe normalmente"
a.falar_oi()