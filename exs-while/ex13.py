import math

# 13
#Crie um programa que calcule o fatorial de um número informado pelo usuário (não permita números negativos).

num = int(input("Digite um valor inteiro positivo: "))
fatorial = 1

if num >= 0:
    if num != 0 and num != 1:
        cont = num
        while cont > 1:
            fatorial *= cont
            cont -= 1
        print(f"o fatorial do numero {num} é {fatorial}")
    else:
        print(f"o número é {num} portanto o fatorial é {fatorial}")
else:
    print(f"o número {num} é inválido, favor digitar um número positivo")