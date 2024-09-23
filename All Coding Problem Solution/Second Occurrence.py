Second Occurrence
harles is given an array A. He wants to find the count of occurrente
of second largest element in the array. Your task is to help him find and return an integer value representing the count of occurrence of
so the second largest element in an array: 
• If the array contains the same elements, then return O
input = [1, 2, 3, 4, 5, 5, 4]
oputput = 2 

***************************** SOlution 1 (Use a Set for Uniqueness)    **************************

arr = [1, 2, 3, 4, 5, 5, 4]
n = len(arr)
s = list(set(arr))
maxa = s[-2]
cnt = 0
for i in range(n):
    if arr[i] == maxa:
        cnt +=1
print(cnt)

***************************** SOlution 2 (Sort the Array)    **************************



def count_second_largest(A):
    A_sorted = sorted(A, reverse=True)
    largest = A_sorted[0]
    second_largest = None
    for num in A_sorted:
        if num < largest:
            second_largest = num
            break
    if second_largest is None:
        return 0
    return A.count(second_largest)

# Example usage
A = [1,2,3,4,5,5,4]
output = count_second_largest(A)
print(output) 



***************************** SOlution 3 (Single Pass (Optimized Approach)**************************
                                          
def count_second_largest(A):
    largest = second_largest = float('-inf')
    count_second_largest = 0
    for num in A:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return 0
    count_second_largest = A.count(second_largest)
    return count_second_largest
A = [1, 2, 3, 4, 5, 5, 4]
output = count_second_largest(A)
print(output) 


             
