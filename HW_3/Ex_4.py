"""
В университет на факультеты A и B поступило равное количество студентов,
а на факультет C студентов поступило столько же, сколько на A и B вместе.
Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9.
Студент сдал первую сессию. Какова вероятность, что он учится:
a). на факультете A
б). на факультете B
в). на факультете C?
"""
x = 1/4*0.8+1/4*0.7+2/4*0.9

# a
p_a = 1/4*0.8/x
print(p_a*100)

# b
p_b = 1/4*0.7/x
print(p_b*100)

# c
p_c = 2/4*0.9/x
print(p_c*100)