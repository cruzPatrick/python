#leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
#ex -> primeiro=Ana ultimo = Souza
nome = input('Me fale seu nome completo: ')
nometam = nome.split()
tam = int(len(nometam))
print(f'Seu primeiro nome é: {nometam[0]} e o último nome é: {nometam[tam-1]}')