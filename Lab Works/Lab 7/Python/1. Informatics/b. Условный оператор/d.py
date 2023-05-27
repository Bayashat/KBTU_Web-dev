"""
https://informatics.msk.ru/mod/statements/view.php?id=276&chapterid=2959#1
Задача №2959. Знак числа
D. Знак числа
"""

x = int(input())

if x == 0:
    print(0)
else:
    print(1 if x > 0 else -1)
