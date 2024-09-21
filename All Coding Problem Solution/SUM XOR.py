You are given an array A of length N. Your task is to find and return an integer value representing the difference between the sum of element at odd index and XOR of element at even index.
Input1: an integer N, representing the length of the array 
Input2: AN integer array A
Example : 
input1: 6
Imput2:{10,5,6,3,7,2}
Output: -1

def difference_sum_xor(N, A):
    odd_sum = 0    # Sum of elements at odd indices
    even_xor = 0   # XOR of elements at even indices

    for i in range(N):
        if i % 2 == 0:  # Even index
            even_xor ^= A[i]
        else:  # Odd index
            odd_sum += A[i]
    
    # Return the difference between odd sum and even xor
    return odd_sum - even_xor

# Example usage:
input1 = 6
input2 = [10, 5, 6, 3, 7, 2]

result = difference_sum_xor(input1, input2)
print(result)  # Output: -1

