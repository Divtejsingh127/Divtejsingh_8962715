# Define a function named 'sum' that takes two parameters 'x' and 'y'
def sum(x, y):
    # Calculate the sum of 'x' and 'y' and assign it to the variable 'sum'
    sum = x + y

    # Check if the calculated sum falls within the range of 15 to 19 (inclusive)
    if sum in range(15, 20):
        return 20  # If the sum falls within the specified range, return 20
    else:
        return sum  # If the sum doesn't fall within the specified range, return the calculated sum
