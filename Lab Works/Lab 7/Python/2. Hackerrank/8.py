"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
Find the Runner-Up Score!
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max = max(arr)
    min = min(arr)

    for i in arr:
        if i > min and i < max:
            min = i
        
    print(min)