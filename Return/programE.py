# program e and f
def compute_quotient(x, y):
    if y == 0 or x == 0:
        return "No arithmetic operation with $0$ value."
    elif x > y:
        return x / y
    else:
        return "First integer is not greater than the second"
    
print(compute_quotient(3, 2))
