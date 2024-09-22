Jack has an array A of length N. He wants to label whether the number in the array is even or odd. Your task is to help him find and return a string with labels even or odd
0 in sequence according to which the numbers appear in the array.
Input Specification:
input1 : An integer array A, representing the array of numbers input2 : A integer N, representing the length of array
Output Specification:
Return a string with labels even or odd in sequence according to which the numbers appear in the array.
Example 1:
input1 : [1,2,3,4,5,6]
input2 : 6
Output : OddEvenOddEvenOddEven

arr= [1,2,4,4]
n = 4
ans = ""
for i in range(n):
    if arr[i] % 2 ==0 :
        ans += "Even"
    else:
        ans += "Odd"
print(ans)

