def lone_sum(a, b, c):
    num_occurrences = {a: 0, b: 0, c: 0}
    for num in (a, b, c):
        num_occurrences[num] = num_occurrences[num] +  1
    unique_nums = [num for num in num_occurrences if num_occurrences[num] == 1]
    return sum(unique_nums)

print(lone_sum(2, 3, 2))