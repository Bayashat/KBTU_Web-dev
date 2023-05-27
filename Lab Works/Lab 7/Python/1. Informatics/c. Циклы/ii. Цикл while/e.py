"""
https://informatics.msk.ru/mod/statements/view.php?id=249&chapterid=3061#1
Задача №3061. Двоичный логарифм
E. Двоичный логарифм
"""
N = int(input()) 

pow = 1 
index = 0 

while(pow < N): 
    pow *= 2
    index += 1

print(index)
