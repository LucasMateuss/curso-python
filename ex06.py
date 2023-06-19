nome = input('Digite seu nome: ')

count = 0
final = len(nome)
novo_nome = '*'

while count < final:
    novo_nome += nome[count]
    novo_nome += '*'
    count += 1

print(novo_nome)

