from random import randint

exponent = int(input('Псс...какая степень уравнения интересует? '))
for i in range(exponent, 0, -1):
    print(f'{randint(0, 100)}*x^{i} + ', end='')
print(f'{randint(0, 100)} = 0')