#Leia um ano e diga se é bissexto
year = int(input('Diga um ano: '))
if (year%4) == 0:
    print(f'{year} é um ano Bissexto')
else:
    print(f'{year} não é um ano Bissexto')