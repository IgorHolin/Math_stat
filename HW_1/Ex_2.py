"""
На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
Код содержит три цифры, которые нужно нажать одновременно.
Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

Общее количество исходов по идее C3/10, у нас одна попытка и кнопки одновременно, значит количество удовлетворяющих
нас решений только одно
"""

from math import factorial

def find():
    return (1/(factorial(10)/(factorial(3)*factorial((10-3)))))*100


print(f'{round(find(),4)}%')
