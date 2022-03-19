from unicodedata import numeric


while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador logico: ')
    sair = input('Você deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
      break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Isso não é um numero! coloque um numero ou saia.')
        continue


    num_1 = int(num_1)
    num_2 = int(num_2)

# + - * /
    if operador == '+':
        print(num_1 + num_2) 
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
         print('Operador inválido!')