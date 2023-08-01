# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for num in args:
        total *= num
    return total

multiplicacao = multiplica(1, 2, 3, 4, 5)

print(multiplicacao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def impar_par(x):
    return f'{x} é par' if x % 2 == 0 else f'{x} é ímpar'

x = int(input('Digite um número: '))

impar_ou_par = impar_par(x)

print(impar_ou_par)

