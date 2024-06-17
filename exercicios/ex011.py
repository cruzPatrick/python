nome = str(input('Qual o seu nome? '))

if(nome == 'Patrick'):
    print('Que nome feio')
elif nome == 'João' or nome == 'Marcos' or nome == 'Mateus' or nome == 'Lucas':
    print('Que nome bonito masculino')
elif nome in 'Ana Maria Mariana Juliana':
    print('Que nome bonito feminino')
elif nome == 'Bruno':
    print('Não falamos do Bruno')
else:
    print(f'Seu nome é bem normal')

print(f'Tenha um bom dia, {nome}!')