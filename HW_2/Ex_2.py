"""
Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?
p = 0.0004
q = 1 - p
n = 5000
k(res_1) = 0
k(res_2) = 2
intensity = 2
"""

from math import factorial as f


def find():
    res_1 = (f(5000)/((f(0)*f(5000))) * 0.0004**0 * (1-0.0004)**5000) * 100
    res_2 = (f(5000)/((f(2)*f(4998))) * 0.0004**2 * (1-0.0004)**4998) * 100
    return round(res_1, 2), round(res_2, 2)

print(f'{find()}%')