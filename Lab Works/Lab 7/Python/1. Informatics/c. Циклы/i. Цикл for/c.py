"""
https://informatics.msk.ru/mod/statements/view.php?id=280&chapterid=335#1
Задача №335. Квадраты
C. Квадраты
"""
from math import sqrt

a = int(input())
b = int(input())

for i in range(a, b + 1):
    if int(sqrt(i)) ** 2 == i:
        print(i)