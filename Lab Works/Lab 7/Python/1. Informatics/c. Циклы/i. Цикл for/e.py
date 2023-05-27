"""
https://informatics.msk.ru/mod/statements/view.php?id=280&chapterid=337#1
Задача №337. Сумма цифр
E. Сумма цифр
"""
x = input()
l = len(x)
x = int(x)

sum = 0

for i in range(l):  
    sum += x % 10
    x = x//10

print(sum)