"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista_compras = []

while True: 
    while True:
        escolha = input('\n(i)nserir\n(a)pagar\n(l)istar\nescolha: ').strip().lower()
        if escolha in 'ial':
            break
        else:
            print('\nDigite uma opção válida')

    if escolha == 'i': 
        produto = input('Digite o produto que deseja adicionar a lista: ')
        lista_compras.append(produto)

    elif escolha == 'a': 
        indice = input('Digite o índice para apagar: ')

        try:
            indice = int(indice)
        
        
