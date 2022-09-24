import random

#Variaveis
aquecedorLigado = False
temperatura = 0
umidade = 0
temperaturaIdeal = 10
#Funções
def getTemperatura():
    global temperatura
    return temperatura
def getUmidade():
    return random.randrange(10,95)
def decreaseTemperatura(): # Deprecated
    global temperatura
    if temperatura > 0:
        temperatura -= 1
def increaseTemperatura(): # Deprecated
    global temperatura
    global temperaturaIdeal
    if temperatura < int(temperaturaIdeal):
        temperatura += 1
def tickTemperatura():
    global temperatura
    global temperaturaIdeal
    global aquecedorLigado

    if aquecedorLigado == True:
        if temperatura < int(temperaturaIdeal):
            temperatura += 1
        elif temperatura > int(temperaturaIdeal):
            temperatura -= 1
    else:
        if temperatura > 0:
            temperatura -= 1
def increaseUmidade():
    global umidade
    umidade += 1
def decreaseUmidade():
    global umidade
    umidade -= 1

def setTemperaturaIdeal(value):
    global temperaturaIdeal
    temperaturaIdeal = value





def aquecedor(estado: str):
    global aquecedorLigado
    if estado == 'on':
        print('Aquecedor Ligado')
        aquecedorLigado = True
    elif estado == 'off':
        print('Aquecedor Desligado')
        aquecedorLigado = False

