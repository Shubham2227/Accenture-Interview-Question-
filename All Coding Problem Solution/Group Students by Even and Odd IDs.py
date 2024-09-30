Maximum Students in Two Groups (or) Divide Students into Even and Odd ID Groups (or) Field Trip Grouping by Student IDs 


You are a teacher organising a field trip for your student.You haves a N students, and you want to divide them into two groups for the trip. However, you have a special requirement: one group should only consist of students with even -numbered IDs, and the other group should only consist of students with odd-numbered IDs and both the groups must be same length. Your task is to find and return an integer value representing the maximum number of students that can be included in both groups. 
input1: An integer value N representing the total number of students 
input2 : An integer array containing the IDs of the students
Return an integer value representing the maximum number of students that can be  included in bothgroups.
input1: 4 
input2: (5,2,3,6) 
Outbut : 2 


def max_students_in_groups(n, ids):
    even_count = 0
    odd_count = 0
    for student in ids:
        if student % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return min(even_count, odd_count)
n = 4
ids = [5, 2, 3, 6]
result = max_students_in_groups(n, ids)
print(result)  # Output: 2
