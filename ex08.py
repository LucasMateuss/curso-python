"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'Morango'
elemento = '*'
palavra_escondida = [elemento] * len(palavra_secreta)
count = 0
acertou = False

while True:
    chute = input('Digite uma letra: ').upper().strip()
    for i, letra in enumerate(palavra_secreta.upper()):
        if chute == letra:
            palavra_escondida[i] = letra
            acertou = True
    
    print(''.join(palavra_escondida))

    count += 1

    if not acertou:
        print('Nenhuma letra encontrada')

    if '*' not in palavra_escondida:
        print(f'Parabéns, você acertou a palavra {palavra_secreta.upper()} em {count} tentativas')
        acertou = True
    