#leia o peso e a altura, calcule o mmc e mostre o status: abaixo de 18.5=abaixo do peso;entre 18.5 e 25=peso ideal; 25 até 30=sobrepeso;30 a 40=obesidade;acima de 40=obesidade mórbida
peso = float(input('Informe o seu peso para calcular o IMC: '))
alt = float(input('Informe o seu altura para calcular o IMC (em metros): '))

imc = peso/alt**2

if imc<18.5:
    print(f'Você está abaixo do peso, seu IMC é {imc:.1f}')
elif imc>=18.5 and imc<25:
    print(f'Você está no peso ideal, seu IMC é {imc:.1f}')
elif imc>=25 and imc<30:
    print(f'Você está em sobrepeso, seu IMC é {imc:.1f}')
elif imc>=30 and imc<40:
    print(f'Você está em obesidade, seu IMC é {imc:.1f}')
else:
    print(f'Você está em obesidade morbida, seu IMC é {imc:.1f}')