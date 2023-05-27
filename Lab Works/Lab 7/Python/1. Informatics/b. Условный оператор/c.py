"""
https://informatics.msk.ru/mod/statements/view.php?id=276&chapterid=2960#1
Задача №2960. Тестирующая система
C. Тестирующая система
"""
import math

# a = input()
# b = int(input())
# if len(x) == 4:
#     if x[0] == x[3] and x[1] == x[2]:
#         print("YES" if a == 1 else "NO")
#     else:
#         print("YES" if a != 1 else "NO")
# else:
#     for i in range(4 - len(x)):
#         x = "0" + x
#         print(x)
#     if x[0] == x[3] and x[1] == x[2]:
#         print("YES" if a == 1 else "NO")
#     else:
#         print("YES" if a != 1 else "NO")

# index = 0
# n_index = -1

# while(int(index) < len(a)//2):
#     i = a[index]
#     j = a[n_index]
#     # print(i, j, index, n_index)
#     if i != j:
#         print("YES" if b != 1 else "NO")
#         break
#     else:
#         index += 1
#         n_index -= 1
    
# if a == "0":
#     print("YES")
# elif a == "000":
#     print("YES")
# elif int(index) == len(a)//2:
#     print("YES" if len(a)!=1 else "NO")

# if a != a[::-1]:
#     print("YES" if b != 1 else "NO")
# else:
#     print("YES")


# 获取输入的两个数字
input1 = input()
input2 = input()

# 判断第一个数字是否是4位数
if len(input1) != 4:
    # 不是4位数的情况下，将逻辑反转
    if input2 == '1':
        print('NO')
    else:
        print('YES')
else:
    # 是4位数的情况下，进行对称判断
    if input1 == input1[::-1]:
        if input2 == '1':
            print('YES')
        else:
            print('NO')
    else:
        if input2 == '1':
            print('NO')
        else:
            print('YES')



