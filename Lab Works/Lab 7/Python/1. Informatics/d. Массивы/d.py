"""
https://informatics.msk.ru/mod/statements/view.php?id=208&chapterid=66#1
Задача №66. Количество элементов, больших предыдущего
D. Количество элементов, больших предыдущего
"""
N = int(input())
arr = input().split()

cnt = 0
prev = int(arr[0])

for i in range(1, N):
    if int(arr[i]) >  prev:
        cnt += 1
    prev = int(arr[i])
    

print(cnt)