def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_palindrome(s):
    return s == s[::-1]
def is_perfect(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n
def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))
n = int(input("Enter a number: "))
print(f"{n} is prime: {is_prime(n)}")
s = input("Enter a string: ")
print(f"{s} is palindrome: {is_palindrome(s)}")
print(f"{n} is perfect: {is_perfect(n)}")
print(f"{n} is armstrong: {is_armstrong(n)}")
print(f"{n} is automorphic: {is_automorphic(n)}")
