#calcule o valor a ser pago de um produto, considerando o seu preço normal e condição de pagamento: a vista dinheiro/cheque=10% de desconto; a vista no cartão=5% de desconto;em até 2x no cartão=preço normal;3x ou mais no cartão=20% de juros
val = float(input('Escreva aqui o valor do produto: '))
form = int(input('Qual a forma de pagamento? 1 - para dinheiro ou cheque 2 - para cartão: '))

if form==int(1):
    print(f'Você escolheu dinheiro/cheque, valor a ser pago é R${(val-(val*0.1)):.2f}')
elif form==int(2):
    par = int(input('Será a vista ou parcelado? 1 - para a vista, 2 - para 2x no cartão ou 3 - para 3x ou mais no cartão: '))
    if par == int(1):
        print(f'O valor a ser pago é: R${(val-(val*.05)):.2f}')
    elif par == int(2):
        print(f'O valor a ser pago é: R${val:.2f}')
    elif par == int(3):
        print(f'O valor a ser pago é: R${(val + (val*.2)):.2f}')
    else:
        print('Erro, insira um valor válido!')
else:
     print('Erro! Insira um valor válido')