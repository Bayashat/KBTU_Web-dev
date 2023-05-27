"""
https://informatics.msk.ru/mod/statements/view.php?id=249&chapterid=3058#1
Задача №3058. Минимальный делитель
B. Минимальный делитель
"""
def find_smallest_factor(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n  


n = int(input())
factor = find_smallest_factor(n)
print(factor)
