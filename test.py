from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для '
           'вычисления квадратного корня из заданного числа')


def calculatesquareroot(number):
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return
    fin = calculatesquareroot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {fin}')


print(message)
calc(25.5)
