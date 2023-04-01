import math

#14
# Crie um programa que diga se o número informado pelo usuário é primo ou não.

num = int(input("Digite um número que deseja saber se é primo: "))

while num < 0:
    print(f"o número digitado foi {num}, números primos não podem ser negativos")
    num = int(input("Digite um número que deseja saber se é primo: "))
if num != 2 and num != 3:
    if num % 2 != 0 and num % 3 != 0:
        print(f"o número {num} é primo")
    else: 
        print(f"o número {num} não é primo")
else:
    print(f"o número {num} é primo")