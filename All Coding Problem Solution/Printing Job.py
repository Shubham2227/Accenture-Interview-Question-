For video solution check out YouTube "Debug with Shubham"  

Printing Job

There is a printing shop where the customers submit their print jobs at regular intervals, and each job takes a fixed amount of time to complete. You are given an 
integer value N denoting the total number of print jobs, and X denoting the time duration after which the next print job arrives.
Your task is to find and return an integer value representing how long the last job will have to wait in the queue considering one print will take exactly 10 minutes. If in case, there is no waiting time then return 0.
Input Specification:
input1: An integer value N representing the number of printing jobs. input2: An integer value X representing the time duration after which the next print job arrives.
SWIF
Output Specification:
Return an integer value representing how long the last job will have to wait in the queue considering one print will take exactly 10 minutes. If in case, 
there is no waiting time then return 0.
Example 1:
input1: 4
inputz: 5
Output : 15
Explanation:
Here, N = 4 and X = 5. Time to complete one print job is 10 mins. So, the time
needed for three prints is 3*10 = 30. The last print job arrives at 15 minutes (3*5). So,
the waiting time is 30 - 15 = 15. Hence, 15 is returned as the output.
  
Example 2:
input1: 3
input2: 10
Output : 0
Explanation:
Here, N=3 and X=10, time to complete one print job is 10 mins. So, the time needed
for 2 prints is 2*10 = 20. The last print job arrives at 20 minutes (2*10). So, the
waiting time is 20 - 20 = 0. Hence, 0 is returned as the output.

**************************** Solution 1 Brute Force ***********************************


def brute_force_solution(N: int, X: int) -> int:
    total_print_time = 0
    arrival_time = 0
    for i in range(1, N): 
        total_print_time += 10  
        arrival_time += X   
    return max(0, total_print_time - arrival_time)
N = 3
X = 10
print(brute_force_solution(N,X))



**************************** Solution 2 best case **********************************

def optimized_solution(N: int, X: int) -> int:
    time_for_previous_jobs = (N - 1) * 10
    last_job_arrival_time = (N - 1) * X
    return max(0, time_for_previous_jobs - last_job_arrival_time)
N = 4
X = 5
print(optimized_solution(N,X))



