"""
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
List Comprehensions
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    filtered_coordinates = [c for c in coordinates if sum(c) != n]

    print(filtered_coordinates)