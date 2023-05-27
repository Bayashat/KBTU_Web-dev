"""
https://informatics.msk.ru/mod/statements/view.php?id=249&chapterid=3060#1
Задача №3060. Точная степень двойки
D. Точная степень двойки
"""
N = int(input())

pow = 1

while(pow < N):
    pow *= 2

if pow == N:
    print("YES")
else:
    print("NO")
