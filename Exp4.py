memo={}
 
def fib(n):
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]

while True: 
    num=int(input("Enter Number: "))
    print("Fibonacci Series of",num,":",fib(num))