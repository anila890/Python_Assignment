def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

prime_numbers = find_prime_numbers(start, end)
print("Prime numbers between", start, "and", end, "are:", prime_numbers)