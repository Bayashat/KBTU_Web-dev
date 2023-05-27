"""
https://informatics.msk.ru/mod/statements/view.php?id=208&chapterid=69#1
Задача №69. Переставить элементы в обратном порядке
G. Переставить элементы в обратном порядке
"""
n = int(input())  
arr = list(map(int, input().split())) 

arr = arr[::-1]

for elem in arr:
    print(elem, end=" ")

    

