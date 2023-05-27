"""
https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2939#1
Задача №2939. Дележ яблок - 2
D. Дележ яблок - 2
"""
N = int(input())
K = int(input())

# remain = K - N * (K//N)
remain = K % N
print(remain)