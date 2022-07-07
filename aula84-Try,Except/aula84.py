# formado mais simples
try:  # similar a if e else
    print(a)
except:
    print('Error')

# mostrando ao python o tipo de error que eu quero tratar
try: #posso usar outro try dentro de try e except como se fosse um if else normal
    # a = {}
    a = []
    print(a)
    # print(a[1])
except NameError as erro:  # aqui seria como se fosse um elif
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro: # tratando dois possiveis erros em apenas um except
    print('Error de index ou chave.')
except Exception as erro:  # seria basicamente um else da vida
    print('Ocorreu um erro inesperado.')
else: #o else sera executado se o try for executado e nao tiver nenhuma exceção(except)
    print("Seu codigo foi executado com sucesso")
finally:
    print('Finalmente') #sempre sera executado em qualquer situação, posso usar para tratar uma exceção nao esperada

print("Bora continuar....")
