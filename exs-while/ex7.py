import math

#7 
# Crie um programa que solicita para o usuário que ele digite 10 valores inteiros. Ao final, imprima a soma de todos os valores digitados.

contagem = 0
nums = 0

while contagem < 10:
    num = int(input("numero?\n"))
    nums = nums + num
    contagem += 1
print(nums)