"""
В первом ящике находится 10 мячей, из которых 7 - белые.
Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча.
Какова вероятность того, что все мячи белые? res_1 = 2 И 2
Какова вероятность того, что ровно два мяча белые? res_2 = 2 И 0/ 1 И 1/ 0 И 2
Какова вероятность того, что хотя бы один мяч белый?
"""
from math import factorial as f


def find():
    a = f(10)/(f(2)*f(10-2)) * 0.7**2 * 0.3**8    # 2/0
    b = (f(10)/(f(1)*f(10-1)) * 0.7**1 * 0.3**9)   # 1/1
    c = (f(10)/(f(0)*f(10-0)) * 0.7**0 * 0.3**10)   # 0/2
    d = (f(11)/(f(0)*f(11-0)) * (9/11)**0 * (2/11)**11)  # 2/0
    e = (f(11)/(f(1)*f(11-1)) * (9/11)**1 * (2/11)**10)  # 1/1
    g = (f(11)/(f(2)*f(11-2)) * (9/11)**2 * (2/11)**9)  # 0/2
    res_1 = (f(10)/(f(7)*f(3)) * 0.7**7 * 0.3**3) * (f(11)/(f(9)*f(2)) * (9/11)**9 * (1-9/11)**2)
    res_2 = a*d + b*e + c*g
    res_3 = (9/11) * 0.7
    return round(res_1*100, 2), res_2*100, round(res_3*100, 2)


print(f'{find()}%')
