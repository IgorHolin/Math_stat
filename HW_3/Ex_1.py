"""
Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
"""
from math import sqrt
arr = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
sr_arif = sum(arr)/len(arr)
summa = 0
for i in range(0, len(arr)):
    d = (arr[i] - sr_arif)**2
    summa += d
smesh_var = summa/len(arr)
nesmesh_var = summa/(len(arr)-1)
smesh_std = sqrt(smesh_var)
nesmesh_std = sqrt(nesmesh_var)
print(f'{sr_arif}\t{smesh_var}\t{nesmesh_var}\t{smesh_std}\t{nesmesh_std}')
