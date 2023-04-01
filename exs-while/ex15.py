import math

#15
# Crie um programa que imprime os números primos entre 0 e 200, imprimindo ao final a soma destes números.

num = 0
primos = 0
somaPrimos = 0

while num < 200:
    if num == 2:
        print("2")
    elif num == 3:
        print("3")
    else:
        if num % 2 != 0 and num % 3 != 0:
            primos = num
            print(primos)
            somaPrimos += primos
    num += 1  
print(somaPrimos + 5)