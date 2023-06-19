""" Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro. """

numero = input('Digite um número: ')

try:
    numero_int = int(numero)

    if numero_int % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
except:
    print('Você não digitou um número inteiro') 



""" Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23. """

horario = input('Digite a hora do dia sem formatação [ 00 ]: ')

try:
    horario_int = int(horario)

    if horario_int >= 7 and  horario_int < 12:
        print('Bom dia')
    elif horario_int <= 18:
         print('Boa tarde')
    else:
        print('Boa noite')          
except:
    print('Você não digitou um número ]')



""" Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".  """

nome = input('Digite seu primeiro nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else: 
    print('Seu nome é muito grande')
