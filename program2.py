
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial_recursive(n - 1)

def main():
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return

        iterative_result = factorial_iterative(number)
        
        recursive_result = factorial_recursive(number)

        print(f"Factorial of {number} (Iterative): {iterative_result}")
        print(f"Factorial of {number} (Recursive): {recursive_result}")

    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()