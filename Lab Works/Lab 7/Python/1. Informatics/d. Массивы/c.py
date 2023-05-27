"""
https://informatics.msk.ru/mod/statements/view.php?id=208&chapterid=65#1
Задача №65. Количество положительных элементов
C. Количество положительных элементов
"""
N = int(input())
arr = input().split()

cnt = 0

for i in arr:
    if int(i) > 0:
        cnt += 1

print(cnt)