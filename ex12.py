"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
count1 = 10
count2 = 11
cpf = '74682489070'
cpf_9_digitos = cpf[:9]
cpf_10_digitos = cpf[:10]
soma1 = 0
soma2 = 0
digito1 = None
digito2 = None

for digito in cpf_9_digitos:
    digito = int(digito)
    soma1 += count1 * digito
    count1 -=1

calculo1 = (soma1 * 10) %11

digito1 = 0 if calculo1 > 9 else calculo1

for digito in cpf_10_digitos:
    digito = int(digito)
    soma2 += count2 * digito
    count2 -=1

calculo2 = (soma2 * 10) % 11

digito2 = 0 if calculo2 > 9 else calculo2

cpf_calculado = f'{cpf_9_digitos}{digito1}{digito2}'

print(f'O CPF {cpf} é válido') if cpf_calculado == cpf else print(f'O CPF {cpf} é inválido')
