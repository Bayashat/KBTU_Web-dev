"""
https://informatics.msk.ru/mod/statements/view.php?id=249#1
Задача №113. Список квадратов
A. Список квадратов
"""
from math import sqrt

N = int(input())

for i in range(1, N+1):  # 0~N
    if int(sqrt(i))**2 == i:
        print(i)
    