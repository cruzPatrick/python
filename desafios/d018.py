import math

angulo = float(input('Escreva um angulo: '))
angulorad = math.radians(angulo)
print(f'O angulo {angulo}, tem {math.sin(angulorad)} de seno, tem {math.cos(angulorad)} de cosseno e tem {math.tan(angulorad)} de tangente')