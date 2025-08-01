print('a','b','c', sep='-')


count = int(input('Enter a number: '))


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(count))  # Example usage of the factorial function