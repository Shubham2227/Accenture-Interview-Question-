There is a ift in your society that can accommodate a maximum weight of X units. The weights of the people planning to use the lift are given in an integer array A of size N. 
Your task is to find and retum an integer value representing the maximum number of people that can use the lift together without exceeding its weight capacity.
Ne Input Specification:
input1: An integer value N representing the number of people planning to use the lift
input2: An integer value X representing the maximum weight capacity of the lift
input3: An integer array A containing the weights of the people planning to use the lift.
Return an integer value representing the maximum number of people
that can use the lift together without exceeding its weight capacity.
Example 1:
inputt : 3
input2: 9
input3 : (5,1,5)
Output : 2
  
Explanation:
Here. X = 9 and the weight array is (5,1,5). Person 1 and person 2 can use
  
the lift together as their total wilight is 6, which is less than the lift's weight capacity. Therefore, the maximum possible number of people that can use the lift together is 2. Hence. 2 is returned as the output.
Example 2:
inputi: 6
inputz: 8
Input3 : (4,3,5,1,1,2)
output: 4 

def max_people_in_lift_two_pointers(N: int, X: int, A: list) -> int:
    if N ==0 :
        return 0
    A.sort()
    cnt = A[0]
    c = 0
    for i in range(1,N):
        if cnt < X:
            cnt += A[i]
            c +=1 
    return c 
        

# Example usage
input1 = 6
input2 = 8
input3 = [4, 3, 5, 1, 1, 2]
print(max_people_in_lift_two_pointers(input1, input2, input3))  
