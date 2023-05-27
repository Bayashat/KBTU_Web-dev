"""
https://informatics.msk.ru/mod/statements/view.php?id=277&chapterid=308#1
Задача №308. Исключающее ИЛИ
C. Исключающее ИЛИ
"""

def Xor(a, n):
    return a ^ n

x, y = map(int, input().split())

print(Xor(x, y))