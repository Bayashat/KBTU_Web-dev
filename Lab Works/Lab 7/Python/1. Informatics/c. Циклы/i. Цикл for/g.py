"""
https://informatics.msk.ru/mod/statements/view.php?id=280&chapterid=339#1
Задача №339. Минимальный делитель
G. Минимальный делитель
"""
x = int(input())

for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break