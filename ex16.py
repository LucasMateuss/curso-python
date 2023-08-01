# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicacao(fator):
    def multiplica(numero):
        return f'O número {numero} multiplicado por {fator} é {numero * fator}'
    return multiplica

duplica = multiplicacao(2)
triplica = multiplicacao(3)
quadruplica = multiplicacao(4)

for valor in range(1, 4):
    print(duplica(valor))
    print(triplica(valor))
    print(quadruplica(valor))