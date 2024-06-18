#Programa que aprove o emprestimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule a prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

emp = float(input('Escreva o valor da casa: '))
sal = float(input('Escreva o seu salário: '))
ano = int(input('Em quantos anos pretende paga? '))

mes = ano*12
exce = emp/float(mes)
corte = sal*0.30

if exce>corte:
    print(f'Desculpa, mas não podemos aceitar o emprestimo, pois 30% de seu salário é menor que um mês de prestação, a prestação seria R${exce:.2f}')
else:
    print(f'O emprestimo foi Aprovado, sua prestação é R${exce:.2f} por ano')