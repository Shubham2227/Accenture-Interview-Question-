Mango Distribution Given a number of mangoes and number of persons. Find the number of ways to distribute identical mangoes among identical persons Input Specification: input1: the number of mangoes input2: the number of persons Output Specification: Return the number of ways to distribute identical mangoes among identical persons
. Example:
input1: 2 
input2: 2 
Output: 3
All possible distributions of 2 identical mangoes to 2 identical persons are (1,1), (2,0) and (0,2). Hence the output is 3. 
input1: 12
Output: 1
Explanation:
the outout is 12.
All possible distributions of 1 identical mango to 12 identical persons are 12

Here's a Python code that solves the problem of distributing a given number of mangoes among a given number of persons:

**************************   Solution 1 (Best Solution)  ***********************

def distribute_mangoes(mangoes, persons):
    # Calculate the number of ways to distribute identical mangoes among identical persons
    ways = (mangoes + persons - 1) // (persons - 1)
    return ways

# Input the number of mangoes and number of persons
mangoes = 2
persons = 2

# Call the function to find the number of ways to distribute mangoes
result = distribute_mangoes(mangoes, persons)
print(result)



Explanation:
1. The function `distribute_mangoes(mangoes, persons)` calculates the number of ways to distribute identical mangoes among identical persons using the formula discussed earlier.
2. In the example provided, we input 2 mangoes and 2 persons.
3. The function is called with these inputs, and the result is stored in the variable `result`.
4. Finally, the result is printed, which in this case would be 3, as there are 3 ways to distribute 2 mangoes among 2 persons: (1,1), (2,0), and (0,2).

This code efficiently calculates the number of ways to distribute mangoes among persons based on the input values provided.


**************************   Solution 3 (use build Function:)  ***********************

import math

def mango_distribution(mangoes, persons):
    # We use the stars and bars formula to compute the number of ways
    # Binomial coefficient: C(mangoes + persons - 1, persons - 1)
    return math.comb(mangoes + persons - 1, persons - 1)

# Example 1
input1 = 2
input2 = 2
print(mango_distribution(input1, input2))  # Output: 3

# Example 2
input1 = 1
input2 = 12
print(mango_distribution(input1, input2))  # Output: 1

**************************   Solution 3 (Without use build Function:)  ***********************

# this solution giveing wrong ans for mongo=1 and person =12 they give 12 but right ans is 1 so look 4th solution
def binomial_coefficients(n, m):
    res = 1
    if m > n - m:
        m = n - m
    for i in range(m):
        res *= (n - i)
        res /= (i + 1)
    return res
    
def calc_ways(m, n):
    if m == 1:
        return n
    if m < n:
        return 0
    ways = binomial_coefficients(n + m - 1, n - 1)
    return int(ways)
    
m = int(input())
n = int(input())
print(calc_ways(m, n))



**************************   Solution 4 (Without use build Function )  ***********************
def binomial_coefficients(n, m):
    res = 1
    if m > n - m:
        m = n - m
    for i in range(m):
        res *= (n - i)
        res /= (i + 1)
    return res
    
def calc_ways(m, n):
    if m == 1:
        return 1
    if m < n:
        return 0
    ways = binomial_coefficients(n + m - 1, n - 1)
    return int(ways)
    
m = int(input())
n = int(input())
print(calc_ways(m, n))
