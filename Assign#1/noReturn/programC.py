# program d
def compute_remainder(x,  y):
    if y < x:
        x, y = y, x  # Swapping using tuple
    print(x % y)
# Display
compute_remainder(3, 2)
