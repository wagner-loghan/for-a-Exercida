# Neste algoritmo estamos calculando a força exercida em uma coluna de liquido

from math import sqrt
from cmath import pi

pi = 3.1415

print('PorFavor, insira os valores abaixo para executarmos o calculo de força!\n')

# Lendo os valores de entrada

altura = float(input('Digite o valor da altura: '))

diametro = float(input('Digite o valor do diametro: '))

gama = float(input('Digite o valor do peso especifico: '))

# Realizando o calculo de força

forca = (pi * gama * sqrt(diametro) * altura) / 4

# Exibindo o valor da força

print('O valor da força é: ', forca)




