def test_sum_function():
    # Test the case where the sum is within the range [15, 19]
    result1 = sum(10, 6)
    expected1 = 20
    assert result1 == expected1, f"Input: 10, 6. Expected Result: {expected1}, Actual Result: {result1}"

    # Test the case where the sum is below the range [15, 19]
    result2 = sum(10, 2)
    expected2 = 12
    assert result2 == expected2, f"Input: 10, 2. Expected Result: {expected2}, Actual Result: {result2}"

    # Test the case where the sum is above the range [15, 19]
    result3 = sum(10, 12)
    expected3 = 22
    assert result3 == expected3, f"Input: 10, 12. Expected Result: {expected3}, Actual Result: {result3}"

def test_sum_function1():
    # Test the case where the sum is within the range [15, 19]
    result1 = sum(10, 8)
    expected1 = 30
    assert result1 == expected1, f"Input: 10, 6. Expected Result: {expected1}, Actual Result: {result1}"

    # Test the case where the sum is below the range [15, 19]
    result2 = sum(10, 2)
    expected2 = 22
    assert result2 == expected2, f"Input: 10, 2. Expected Result: {expected2}, Actual Result: {result2}"

    # Test the case where the sum is above the range [15, 19]
    result3 = sum(10, 12)
    expected3 = 25
    assert result3 == expected3, f"Input: 10, 12. Expected Result: {expected3}, Actual Result: {result3}"

# Define the sum function
def sum(x, y):
    # Calculate the sum of 'x' and 'y' and assign it to the variable 'sum'
    sum_val = x + y

    # Check if the calculated sum falls within the range of 15 to 19 (inclusive)
    if sum_val in range(15, 20):
        return 20  # If the sum falls within the specified range, return 20
    else:
        return sum_val  # If the sum doesn't fall within the specified range, return the calculated sum


# Call the test function to execute the test cases
test_sum_function()