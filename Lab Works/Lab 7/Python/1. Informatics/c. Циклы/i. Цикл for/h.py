"""
https://informatics.msk.ru/mod/statements/view.php?id=280&chapterid=340#1
Задача №340. Делители числа
H. Делители числа
"""
x = int(input())

for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")