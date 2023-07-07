"""
Corrigindo possíveis problemas em nosso código
"""
import re
import sys

entrada = input('CPF [746.824.890-70]: ')

cpf_entrada = re.sub(r'[^0-9]', '', entrada)

cpf_sequencial = entrada == entrada[0] * len(entrada)

if cpf_sequencial:
    print('Você digitou um valor sequencial')
    sys.exit()

cpf_9_digitos, cpf_10_digitos = cpf_entrada[:9], cpf_entrada[:10]

count1, count2 = 10, 11

soma1, soma2 = 0, 0

digito1, digito2 = None, None


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

print(f'O CPF {cpf_entrada} é válido') if cpf_calculado == cpf_entrada else print(f'O CPF {cpf_entrada} é inválido')
