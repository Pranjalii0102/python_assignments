def fib(n):
    if n < 0:
        return "Fibonacci number is not defined for negative values."

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b

n = int(input("Enter the value of n: "))

result = fib(n)

print("The", n, "th Fibonacci number is:", result)