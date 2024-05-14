#leia uma frase pelo teclado e mostre quantas vezes aparece a letra a, em que posição aparece a primeira vez, em que posição ela aparece a ultíma vez
frase = input('Escreva uma frase: ')
print(f'A frase tem {frase.count('a')} de a, a primeira vez que aparece é em {frase.find('a')} e a ultima vez é em {frase.rfind('a')}')