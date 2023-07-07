"""
Desenvolvendo um gerador de CPF
"""
import random

cpf_9_digitos = ''

for num in range(9):
    cpf_9_digitos += str(random.randint(0, 9))

count1, count2 = 10, 11

soma1, soma2 = 0, 0

digito1, digito2 = None, None


for digito in cpf_9_digitos:
    soma1 += count1 * int(digito)
    count1 -=1

calculo1 = (soma1 * 10) %11

digito1 = 0 if calculo1 > 9 else calculo1

cpf_10_digitos = cpf_9_digitos + str(digito1)

for digito in cpf_10_digitos:
    soma2 += count2 * int(digito)
    count2 -=1

calculo2 = (soma2 * 10) % 11

digito2 = 0 if calculo2 > 9 else calculo2

cpf_calculado = f'{cpf_9_digitos}{digito1}{digito2}'

cpf = f'{cpf_9_digitos}{digito1}{digito2}'

print(cpf)