#crie um programa que leia o nome de uma pessoa e mostra: todas as letras maiusculas, todas minusculas, total de letras sem espaço, quantas letras tem o primeiro nome

nome = input('Digite o seu nome: ')
print(f'{nome.upper()} fica assim com tudo maiúsculo')
print(f'{nome.lower()} fica assim com tudo minúsculo')
nospace = nome.split()
print(f'{nome} tem {len(''.join(nospace))} letras')
print(f'{nospace[0]} tem {len(nospace[0])} letras')
