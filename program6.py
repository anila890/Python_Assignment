
def fibonacci(n):
    
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the number of terms: "))

fib_sequence = fibonacci(n)

print(", ".join(map(str, fib_sequence)))