"""
https://informatics.msk.ru/mod/statements/view.php?id=280#1
Задача №333. Четные числа
A. Четные числа
"""

a = int(input())
b = int(input())

for i in range(a, b+1):
    if i%2==0:
        print(i, end=' ')