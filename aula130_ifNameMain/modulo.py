def soma(x: float, y: float) -> float:
    return x + y


# se eu executo o meu codigo aonde eu criei ele, o python chama de main
# ja se eu import o meu codigo para outro local e executo ele, o python vai mostrar de onde ele veio

"possa fazer desasa maniera"
# se meu arquivo estiver sendo executado diretamente voce pode executar esse print aqui
# if __name__ == '__main__':
#     print(soma(10, 20))

"ou criando uma função chamada main e executando ela, dessa maneira aqui"


def main() -> None:
    print(soma(20, 40))


if __name__ == '__main__':
    main()
