#Distancia de uma viagem em km, calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas

dis = float(input('Fale a distância da viagem em km: '))
if dis<=200:
    print(f'O valor a ser pago da viagem é R${dis*0.50:.2f}')
else:
    print(f'O valor a ser pago da viagem é de R${dis*0.45:.2f}')
print('Boa Viagem!')