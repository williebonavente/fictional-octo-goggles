def twoDiff(x,  y):
    if x < y:
        x, y = y, x  # Swapping using tuple
    print(x - y)
        
# Display
print(twoDiff(100, 30))
print(twoDiff(30, 33))
