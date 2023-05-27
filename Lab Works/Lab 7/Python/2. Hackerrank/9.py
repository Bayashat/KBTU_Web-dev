"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
Nested Lists
"""
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))

    # Find the second lowest score
    second_lowest_score = sorted(set([score for name, score in students]))[1]

    # Create a dictionary of students with the same score
    students_dict = {score: [name for name, score_ in students if score_ == score] 
                     for score in set([score_ for name_, score_ in students])}

    # Get the names of students with the second lowest score
    names = students_dict[second_lowest_score]

    # Print the names in alphabetical order
    for name in sorted(names):
        print(name)
