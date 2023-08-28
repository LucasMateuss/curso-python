# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
quantidadeAcertos = 0

for pergunta in perguntas:
    print(f"\nPergunta: {pergunta['Pergunta']}")

    for num, i in enumerate(pergunta['Opções']):
        print(f"{num + 1}) {i}")

    resposta = input(f"\nEscolha: ")

    respostaInt = None

    acertou = False
    opcoes = pergunta['Opções']

    if resposta.isdigit(): 
        respostaInt = int(resposta)

    if respostaInt is not None:
        if respostaInt >= 0 and respostaInt < len(opcoes):
            if opcoes[respostaInt - 1] == pergunta['Resposta']:
                acertou = True

    if acertou:
        quantidadeAcertos += 1
        print('\nAcertou 👍')

    else:
        print('\nErrou ❌')
    
print(f"Você acertou {quantidadeAcertos} de {len(perguntas)}")

    
    
