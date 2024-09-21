Special fibonacci
alex is exporling a series and she come across a special series, in which
f(N) = f(N-1) * f(N-1) + (f(N-2)*f(N-2))
where f(0)=1,f(1)=1 
your taask is to help alex and return an integer value representing the N" number in this special series.
Expected return the output modulo 47.

def special_fibonacci(N):
    # Base cases
    if N == 0 or N == 1:
        return 1

    # Initialize the first two numbers in the series
    f0 = 1
    f1 = 1

    # Loop to calculate the N-th number in the series
    for i in range(2, N + 1):
        fn = (f1 * f1 + f0 * f0) % 47  # Apply modulo 47
        f0 = f1  # Update f(N-2) to f(N-1)
        f1 = fn  # Update f(N-1) to f(N)

    return f1

# Example usage:
N = 2
result = special_fibonacci(N)
print(result)
