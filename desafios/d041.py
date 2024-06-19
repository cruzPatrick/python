#programa que leia o ano de nascimento e mostre sua categoria de acordo com a idade: até 9 = mirim; ate 14 = infantil; ate 19=junior; ate 20=senior;acima=master
import time

ano = int(input('Em que ano você nasceu: '))
anoA = time.localtime()
clas = int(anoA.tm_year) - ano

if clas<9:
    print('seu atleta é mirim')
elif clas<=14:
    print('seu atleta é infantil')
elif clas<=19:
    print('seu atleta é junior')
elif clas<=20:
    print('Seu atleta é senior')
else:
    print('Seu atleta é master')