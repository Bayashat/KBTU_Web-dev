"""
https://informatics.msk.ru/mod/statements/view.php?id=208&chapterid=64#1
Задача №64. Вывести четные элементы
B. Вывести четные элементы
"""
N = int(input())
arr = input().split()

for i in range(1, N, 2):
    print(arr[i], end=" ")