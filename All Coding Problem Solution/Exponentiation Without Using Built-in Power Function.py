def exponent(a, b):
    ans = 1
    for i in range(1,b+1):
        ans *= a
    return ans
a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
result = exponent(a, b)
print(f"{a} raised to the power of {b} is: {result}")
