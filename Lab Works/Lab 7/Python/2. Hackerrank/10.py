"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
Finding the percentage
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    scores_ = student_marks[query_name]

    total = sum(scores)

    print(f"{total/len(scores_):.2f}")