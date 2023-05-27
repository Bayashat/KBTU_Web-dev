"""
https://informatics.msk.ru/mod/statements/view.php?id=280&chapterid=341#1
Задача №341. Количество делителей
I. Количество делителей
"""
import math

x = int(input())  # 16
cnt = 0 # 4
for i in range(1, int(math.sqrt(x))+1):  # 4
    if x % i == 0:
        cnt += 1
        if i != x // i:
            cnt += 1
print(math.sqrt(32))