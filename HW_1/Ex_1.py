from math import factorial

# 1 Задание
"""
По идее у нас есть вероятность вытянуть 4 карты крести, то есть С 4/12, общее число вероятностей С 4/52,
значит в теории конечная вероятность у нас (С 4/12) / (С 4/52)
"""
def find_a():
    a = factorial(13)/(factorial(4) * factorial(13-4))
    b = factorial(52)/(factorial(4) * factorial(52-4))
    return a/b*100

print(f'{find_a()}%')


"""
В данном пункте убираем одну карту крести и вводим вероятность вытянуть 1 туз из 4 в колоде, т.е. С 1/4
"""
def find_b():
    a = factorial(13)/(factorial(3) * factorial(13-3))
    b = factorial(52)/(factorial(4) * factorial(52-4))
    c = factorial(4)/(factorial(1) * factorial(4-1))
    return (a*c)/b*100

print(f'{find_b()}%')


