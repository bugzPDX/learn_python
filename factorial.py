# calculates the factorial of a number

n = input("Enter a number: ")
product = 1

while n >= 1:
    product *= n
    n -= 1
print product

n = input("Enter a number: ")
product = 1

for i in range(1, n+1):
    product *= n
    n -= 1
print product


def factorial(n):
    n = input("Enter a number: ")
    if(n == 1):
        ans = 1
    else:
        ans = n*factorial(n - 1)
    return ans
factorial()
