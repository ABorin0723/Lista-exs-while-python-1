import math

#8
# Crie um programa que pergunta para o usuário (via Teclado) quantos números ele irá digitar e armazena em uma variável chamada quant. Logo após, faça
# com que o usuário digite quant números inteiros, e para cada número digitado imprima na tela se o número é negativo, positivo ou zero.

cont = 0
quant = int(input("quantos números?"))

while cont < quant:
    num = int(input("qual o número?"))
    if num < 0:
        print("o numero é negativo")
    elif num > 0:
        print("o número é positivo")
    else:
        print("o número é 0")
    cont += 1