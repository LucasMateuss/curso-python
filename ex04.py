nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
idade_int = int(idade)

if nome and idade:
    print(
f"""Seu nome é: {nome}
Seu nome invetido é: {nome[::-1]}
Seu nome tem {len(nome)} letras
A primeira letra do seu nome é {nome[0]}
A última letra do seu nome é {nome[-1]}""")
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
else:
    print('Desculpe, você não preencheu os campos corretamente')