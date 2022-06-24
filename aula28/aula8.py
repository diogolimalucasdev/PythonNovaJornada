num1 = input("digite um  numero: ")
num2 = input("digite um outro numero: ")

# isnumeric isdigit isdecimal

"verificar se é um numero positivo"
# print(num1.isdecimal())  # ele  da false se o numero for negativo ou letra
# print(num2.isdecimal())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)

else:
    print("nao pode converter os numeros para realizar contas !")
