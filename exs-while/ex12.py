import math

#12
# Crie um programa que pede para o usuário digitar números positivos via Teclado. 
# Quando o usuário digitar um número negativo, informe a média de todos os números que ele informou.

num = int(input("valores inteiros positivos: "))
positivos = 0
media = 0

while num > 0:
    num = int(input("valores inteiros positivos: "))
    if num < 0:
        print(positivos/media)
        break
    positivos += num
    media += 1