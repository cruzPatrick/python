amigos = []
tam = int(input ('Quantas pessoas você quer adicionar na lista?\n'))
'''Precisa de conversão de base pois input sempre será em string e não em qualquer coisa se eu não deixar explícito'''

for i in range(tam):
    nome = input(f'Digite o nome do amigo {i+1}:\n')
    amigos.append(nome)
    
print(f'\n {amigos}')

'''Preciso colocar {} quando for uma variável e precisa do f antes'''
'''Esse f é de formatted string ou f-string'''