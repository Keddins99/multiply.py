def multiply(a, b):
    # Base case: if either a or b is 1, return the other number
    if a == 1:
        return b
    if b == 1:
        return a
    # Recursive case: multiply a by (b - 1) and add a to the result
    return a + multiply(a, b - 1)



