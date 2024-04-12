quest = input('Digite algo: ')
print('{} é um valor: {}'.format(quest, type(quest)))
print('{} é Letra? {}'.format(quest, quest.isalpha()))
print('{} é número? {}'.format(quest, quest.isnumeric()))
print('{} é um valor alfanumerico? {}'.format(quest, quest.isalnum()))
print('{} é todo maiusculo? {}, é todo minusculo? {}'.format(quest, quest.isupper(),quest.islower()))
print('{} é só tem espaços? {}'.format(quest, quest.isspace()))
print('{} é capitalizada? {}'.format(quest, quest.istitle))
#print(f'A {quest} é uma letra {quest.isalpha()}? e pode ser um número {quest.isnumeric()}') outra forma de fazer