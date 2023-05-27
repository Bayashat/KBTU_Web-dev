"""
https://informatics.msk.ru/mod/statements/view.php?id=277#1
Задача №306. Минимум 4 чисел
A. Минимум 4 чисел
"""

arr = list(map(int, input().split())) 

def find_min(arr:list):
    return min(arr)

print(find_min(arr))