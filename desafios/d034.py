#pergunte o salário do funcionario e calcule seu aumento, para salarios superiores a 1250,00 calcule aumento de 10%, para inferioes ou iguais, o aumento é 15%

sal = float(input('Me fale seu salário: '))

if sal>1250.00:
    print(f'Seu salário de R${sal} foi aumentado para R${sal+(sal*0.1):.2f}')
else:
    print(f'Seu salário de R${sal} foi aumentado para R${sal+(sal*0.15):.2f}')