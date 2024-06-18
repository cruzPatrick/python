import time
#leia o ano de nascimento e informe de acordo com sua idade: -Se ele ainda vai se alistar, - Se é a hora de se alistar, -Se já passou do tempo de alistamento. Tambem deverá mostrar o tempo que falta ou que passou do prazo

ano = int(input('Em que ano você nasceu: '))
anoA = time.localtime()

alis = int(anoA.tm_year) - ano

'''
if alis < 16:
    print('Ainda vai ter que se alistar')
    print(f'faltam {17-alis} anos para se alistar')
elif alis>16 or alis<=18:
    print('Vai ter que se alistar')
else:
    print('Já passou do tempo de se alistar')
    print(f'Se passaram {alis-18} anos do alistamento')

'''

if alis>18:
    print('Já passou do tempo de se alistar')
    print(f'Se passaram {alis-18} anos do alistamento')
elif alis<=18 and alis>=17:
    print('Vai ter que se alistar')
else:
    print('Ainda vai ter que se alistar')
    print(f'faltam {17-alis} anos para se alistar')