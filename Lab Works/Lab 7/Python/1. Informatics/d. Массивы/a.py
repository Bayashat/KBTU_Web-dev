"""
https://informatics.msk.ru/mod/statements/view.php?id=208#1
Задача №63. A[0], A[2], A[4], ...
A. A[0], A[2], A[4], ...
"""
N = int(input())
arr = input().split()

for i in range(0, N, 2):
    print(arr[i])