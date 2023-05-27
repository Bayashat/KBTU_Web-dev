"""
https://informatics.msk.ru/mod/statements/view.php?id=276&chapterid=253#1
Задача №253. Високосный год
B. Високосный год
"""

x = int(input())

if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print("YES")
else:
    print("NO")
