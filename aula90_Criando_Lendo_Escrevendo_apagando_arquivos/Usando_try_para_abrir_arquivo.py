try:
    file = open('def.txt', 'w+')
    file.write('Linha 1')
    file.seek(0)
    print(file.read())
finally:
    file.close()