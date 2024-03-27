# program d
def compute_remainder(x,  y):
    if y < x:
        x, y = y, x  # Swapping using tuple
    return x % y
# Display
print(compute_remainder(100, 30))
print(compute_remainder(30, 33))
