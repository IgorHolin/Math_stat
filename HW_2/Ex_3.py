"""
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
n = 144
k = 70
p,q = 0.5
"""
from math import factorial as f


def find():
    a = (f(144)/(f(70)*f(144-70)) * 0.5**70 * 0.5**74) * 100
    return round(a, 2)


print(f'{find()}%')
