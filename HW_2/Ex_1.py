"""
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
"""

from math import factorial as f
def find():
    a = (f(100)/(f(85)*f(15)))* 0.8**85 * 0.2**15
    b = (80**85)/f(85)*2.72**(-80)
    return(round(a,4)*100,round(b,4)*100)

print(f'{find()}%')
