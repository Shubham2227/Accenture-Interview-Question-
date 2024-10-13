write a program to find the sum of all even number in given array 

def even(arr,n):
    ans = 0
    for i in range(n):
        if arr[i]%2 ==0:
            ans += arr[i]
    return ans 
arr = [1,2,3,4,5,6,7,8]
n = len(arr)
print(even(arr,n))
