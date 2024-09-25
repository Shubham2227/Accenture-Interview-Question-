Qualifying Score
There is a competition in a school. A qualifying score has been set as the cut-off for students to take part in this competition.
There are N subjects taught in a class. The marks obtained in each subject for semesters 1 and 2 are given in the form of two arrays S1 and S2 respectively. 
The qualifying score is calculated in the following way:
Step 1: Subtract the marks obtained in the i-th subject in Semester 1 (S1[i]) from the marks obtained in the i-th subject in Semester 2 (S2[i]), i.e., S2[i] - S1[i] 
  for each i where 0 <= i < N.
Step 2: Consider the differences obtained after subtraction and add the top P differences (the ones with the highest values). This sum becomes the student's qualifying score.
The goal is to determine if the student's qualifying score is greater than or equal to 35. If so, the student qualifies for the competition, otherwise, they are disqualified.
Your task: Write a function to find and return a string value, either Qualified followed by the score achieved, or "Disqualified" . followed by the score achieved 

Input Specification:
input1: An integer N, representing the number of subjects taught in the class.
input2: An integer P, representing the maximum number of subjects that can be considered to calculate the qualifying score.
input3: An integer array S1 of size N, representing the marks obtained in the N subjects in Semester 1.
input4: An integer array S2 of size N, representing the marks obtained in the N subjects in Semester 2.
Output Specification:
Return a string in the format: Qualified followed by the score achieved, or Disqualified followed by the score achieved, separated by a space.
Example: 
input1 = 5
input2 = 3
input3 = [5, 10, 15, 20, 25]
input4 = [15, 30, 20, 30, 25]
Output: Qualified 40

Explanation:
After subtraction: S2 - S1 = [15 - 5, 30 - 10, 20 - 15, 30 - 20, 25 - 25] = [10, 20, 5, 10, 0].
We can select the top 3 differences: 20, 10, 10.
The sum of the top 3 differences is 20 + 10 + 10 = 40.
Since 40 >= 35, the student qualifies 


************************************ Brute Force Approach: ********************

from itertools import combinations

def brute_force_solution(N, P, S1, S2):
    # Step 1: Calculate the differences
    differences = [S2[i] - S1[i] for i in range(N)]
    
    # Step 2: Generate all combinations of P elements
    for comb in combinations(differences, P):
        # Step 3: Calculate the sum of the combination
        if sum(comb) >= 35:
            return f"Qualified {sum(comb)}"
    
    # If no combination qualifies
    return "Disqualified 0"


************************************ Solution -1 (Sorting Approach (Greedy): ********************
      
def qualifying_score(N, P, S1, S2):
    differences = [S2[i] - S1[i] for i in range(N)]
    differences.sort(reverse=True)
    qualifying_score = sum(differences[:P])
    if qualifying_score >= 35:
        return f"Qualified {qualifying_score}"
    else:
        return f"Disqualified {qualifying_score}" 

    

.# .Example usage:
N = 5
P = 3
S1 = [5, 10, 15, 20, 25]
S2 = [15, 30, 20, 30, 25]

print(qualifying_score(N, P, S1, S2))  # Output: Qualified 40


