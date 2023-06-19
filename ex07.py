numero1 = ''
numero2 = ''
continuar = 'S'
while continuar == 'S':
    while type(numero1) == str or type(numero2) == str:
        numero1 = input('Digite um número: ')
        numero2 = input('Digite um número: ')

        try:
            numero1 = float(numero1)
            numero2 = float(numero2)
        except:
            print('Você não digitou um número. Tente novamente')
    
    print('Digite o que você deseja fazer:\n[ 0 ] Soma\n[ 1 ] Subtração\n[ 2 ] Multiplicação\n[ 3 ] Divisão\n [ 4 ] Módulo\n[ 5 ] Dividendo')
    escolha = input('Escolha: ')

    if escolha == 0: 
        print(f'A soma de {numero1} + {numero2} é {numero1 + numero2}')
    elif escolha == 1:
        print(f'A subtração de {numero1} - {numero2} é {numero1 - numero2}')
    elif escolha == 2:
        print(f'A multiplicação de {numero1} x {numero2} é {numero1 * numero2}')
    elif escolha == 3:
        print(f'A divisão de {numero1} / {numero2} é {numero1 / numero2}')
    elif escolha == 4:
        print(f'O módulo de {numero1} por {numero2} é {numero1 % numero2}')
    else:
        print(f'O dividendo de {numero1} por {numero2} é {numero1 // numero2}')

    continuar = input

    