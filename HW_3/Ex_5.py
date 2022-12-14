"""
Устройство состоит из трех деталей.
Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
Какова вероятность того, что в первый месяц выйдут из строя:
а). все детали
б). только две детали
в). хотя бы одна деталь
г). от одной до двух деталей?
"""
p = 1/3*0.1+1/3*0.2+1/3*0.25
q = 1-p

# a
p_a = (0.1*0.2*0.25)/p
print(p_a*100)

# b
p_b = ((0.1/p) * (0.2/p) * (0.25/q)) + ((0.1/p) * (0.2/q) * (0.25/p)) + ((0.1/q) * (0.2/p) * (0.25/p))
print(p_b*100)

# c
p_c = ((0.1/p) * (0.2/q) * (0.25/q)) + ((0.1/q) * (0.2/p) * (0.25/q)) + ((0.1/q) * (0.2/q) * (0.25/p))
print(p_c*100)
