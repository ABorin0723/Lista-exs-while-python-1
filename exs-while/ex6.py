import math

#6
# Crie um programa que pede para o usuário digitar 20 números com ponto
# flutuante pelo teclado. Ao final, seu programa deve imprimir todos os números
# digitados. Dica: armazene-os em uma string e concatene os valores digitados. No final,
# imprima a string.

contagem = 0
nums = ""

while contagem < 10:
    num = float(input("numero?\n"))
    nums = nums + str(num) + "\n"
    contagem += 1
print(nums)