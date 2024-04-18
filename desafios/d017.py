import math

catO = float(input('Escreva o valor do cateto oposto: '))
catA = float(input('Escreva o valor do cateto adjacente: '))
hipo = (catO**2) + (catA**2)
print(f'A hipotenusa desse triangulo é {math.sqrt(hipo)}')