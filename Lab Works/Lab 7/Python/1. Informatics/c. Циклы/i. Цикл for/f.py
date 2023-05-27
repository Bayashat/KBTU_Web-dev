"""
https://informatics.msk.ru/mod/statements/view.php?id=280&chapterid=338#1
Задача №338. Переверни число
F. Переверни число
"""

x = input()

result = x[::-1]
while(result.startswith("0")):
    result = result.replace('0','',1)

print(result)