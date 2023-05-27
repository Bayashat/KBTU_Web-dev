"""
https://informatics.msk.ru/mod/statements/view.php?id=280&chapterid=334#1
Задача №334. Остаток
B. Остаток
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b + 1):
    if(i%d==c):
        print(i, end=" ")