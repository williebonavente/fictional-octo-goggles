# program d
def compute_quotient(x,  y):
    if y < x:
        x, y = y, x  # Swapping using tuple
    print(x / y)
# Display
compute_quotient(3, 2)
compute_quotient(4, 3)
