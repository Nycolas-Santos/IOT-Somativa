import random

#Funções
def temperatura():
    return random.randrange(1, 34)


def umidade():
    return random.randrange(10, 100)


def aquecedor(estado: str):
    if estado == 'on':
        print('Aquecedor Ligado')
    elif estado == 'off':
        print('Aquecedor Desligado')

