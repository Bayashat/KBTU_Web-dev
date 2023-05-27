"""
https://informatics.msk.ru/mod/statements/view.php?id=277&chapterid=307#1
Задача №307. Степень
B. Степень
"""

def power(a, n):
    return a ** n

a, n = map(float, input().split())

print(power(a, int(n)))