'''
The steps to solve this problem:

1- Read the input and store the student names and grades in a nested list.
2- Sort the nested list based on the grades.
3- Find the second lowest grade.
4- Collect the names of students who have the second lowest grade.
5- Sort the names alphabetically.
6- Print the names of students with the second lowest grade.
'''

if __name__ == '__main__':
    students = []
    second_lowest_grade = float('inf')
    lowest_grade = float('inf')
    
    # Read input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
        # Update lowest and second lowest grades
        if score < lowest_grade:
            second_lowest_grade = lowest_grade
            lowest_grade = score
        elif score != lowest_grade and score < second_lowest_grade:
            second_lowest_grade = score
    
    # Find students with second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print the names
    for name in second_lowest_students:
        print(name)