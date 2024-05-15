#leia a velocidade de um carro se ultrapassar 80 ele foi multado, a multa custa 7r$ por cada km por limite acima 
vel = float(input('Qual a sua velocidade? '))
if vel>80.00:
    print('Você ultrapassou o limete permitido')
    print(f'Sua multa é de R${(vel-80)*7:.2f}' )
else:
    print('Sua velocidade está no limite permitido')
print('Boa viagem!')