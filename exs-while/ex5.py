import math

#5 
# Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final, imprima quantos torcedores torcem para o Grêmio.

contagem = 0
gremio = 0

while contagem < 10:
    time = input("seu time? ")
    if time == "gremio":
        gremio += 1
    contagem += 1
print(gremio)