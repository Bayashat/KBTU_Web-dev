"""
https://informatics.msk.ru/mod/statements/view.php?id=280&chapterid=345#1
Задача №345. Нули
M. Нули
"""

N = int(input())
cnt = 0

for i in range(N):
    num = input()
    if num == '0':
        cnt += 1

print(cnt)
