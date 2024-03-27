# program e and f
def compute_quotient(x, y):
    if y == 0 or x == 0:
        print("No arithmetic operation with $0$ value.")
    elif x > y:
        print(x / y)
    else:
        print("First integer is not greater than the second")
    
compute_quotient(3, 2)
