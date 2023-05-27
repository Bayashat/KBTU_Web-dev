"""
https://informatics.msk.ru/mod/statements/view.php?id=208&chapterid=67#1
Задача №67. Есть ли два элемента с одинаковыми знаками
E. Есть ли два элемента с одинаковыми знаками
"""
N = int(input())
arr = input().split()

arr = ["+" if int(num) > 0 else "-" for num in arr]

def check():
    i = 1
    prev = arr[0]
    while(i < N):
        if arr[i] == prev:
            return "YES"
        prev = arr[i]
        i += 1
    return "NO"

print(check())
    

