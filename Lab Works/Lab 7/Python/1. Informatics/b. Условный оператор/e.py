"""
https://informatics.msk.ru/mod/statements/view.php?id=276&chapterid=293#1
Задача №293. Какое из чисел больше?
E. Какое из чисел больше?
"""

a = int(input())
b = int(input())
if a == b:
    print(0)
else:
    print(1 if a > b else 2)
