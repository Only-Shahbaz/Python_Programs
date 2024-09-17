def fibonacci_series(n):
    a, b = 0, 1
    series = []
    
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series

# Specify the number of terms you want in the Fibonacci series
num_terms = int(input("Enter your Number : "))

# Generate and print the Fibonacci series
fib_series = fibonacci_series(num_terms)
print(f"Fibonacci series up to {num_terms} terms: {fib_series}")
