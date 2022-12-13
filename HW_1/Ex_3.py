"""
В ящике имеется 15 деталей, из которых 9 окрашены.
Рабочий случайным образом извлекает 3 детали.
Какова вероятность того, что все извлеченные детали окрашены?
"""

from math import factorial

def find():
    a = factorial(15)/(factorial(3)*factorial(15-3))  # общее число вероятностей
    b = factorial(9)/(factorial(3)*factorial(9-3))  # вероятность извлечь 3 из 9 окрашенных
    return b/a*100

print(f'{round(find(),4)}%')