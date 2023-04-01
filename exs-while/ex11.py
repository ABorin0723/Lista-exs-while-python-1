import math

#11
# Crie um programa que imprima a soma dos valores pares e a soma dos 
# valores ímpares entre dois números quaisquer digitados pelo usuário.

val1 = int(input("digite o valor 1 "))
val2 = int(input("digite o valor 2 "))

somaPares = 0       
somaImpares = 0

if val1 < val2:
    cont = val1
    while cont < val2:
        if cont % 2 == 0:
            somaPares += cont
        else:
            somaImpares += cont
        cont += 1
    print(somaPares)
    print(somaImpares)
else:
    print("erro, o valor 1 deve ser menor que o valor 2")