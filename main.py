def multiply(a, b):

    if a == 0 or b == 0:
        return 0

    return a + multiply(a, b - 1)

num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))
result = multiply(num1, num2)
print(f"The product of {num1} and {num2} is {result}")
