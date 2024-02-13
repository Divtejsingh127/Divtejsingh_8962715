def check_integer_string(text):
    # Remove leading and trailing whitespaces from the input string using the 'strip()' function
    text = text.strip()

    # Check if the length of the cleaned text is less than 1
    if len(text) < 1:
        return "Input a valid text"  # If the text length is less than 1, return a message asking for valid input
    else:
        # Check if all characters in the cleaned text are digits (0-9), indicating an integer
        if all(text[i] in "0123456789" for i in range(len(text))):
            return "The string is an integer."  # If all characters are digits, return a message indicating an integer
        # Check if the text starts with a '+' or '-' and all subsequent characters are digits
        elif (text[0] in "+-") and all(text[i] in "0123456789" for i in range(1, len(text))):
            return "The string is an integer."  # If the conditions for a signed integer are met, return an integer message
        else:
            return "The string is not an integer."  # If none of the conditions are met, return a non-integer message

def test_check_integer_string():
    # Test with a valid integer string
    result1 = check_integer_string("123")
    expected1 = "The string is an integer."
    assert result1 == expected1, f"Test case 1 failed: Expected '{expected1}', but got '{result1}'"

    # Test with a valid signed integer string
    result2 = check_integer_string("+456")
    result3 = check_integer_string("-789")
    expected2 = expected3 = "The string is an integer."
    assert result2 == expected2, f"Test case 2 failed: Expected '{expected2}', but got '{result2}'"
    assert result3 == expected3, f"Test case 3 failed: Expected '{expected3}', but got '{result3}'"

    # Test with a non-integer string
    result4 = check_integer_string("abc")
    expected4 = "The string is not an integer."
    assert result4 == expected4, f"Test case 4 failed: Expected '{expected4}', but got '{result4}'"

    # Test with an empty string
    result5 = check_integer_string("")
    expected5 = "Input a valid text"
    assert result5 == expected5, f"Test case 5 failed: Expected '{expected5}', but got '{result5}'"


def test_check_integer_string1():
    # Test with a valid integer string
    result1 = check_integer_string("abc")
    expected1 = "The string is an integer."
    assert result1 == expected1, f"Test case 1 failed: Expected '{expected1}', but got '{result1}'"

    # Test with a valid signed integer string
    result2 = check_integer_string("+456b")
    result3 = check_integer_string("-789c")
    expected2 = expected3 = "The string is an integer."
    assert result2 == expected2, f"Test case 2 failed: Expected '{expected2}', but got '{result2}'"
    assert result3 == expected3, f"Test case 3 failed: Expected '{expected3}', but got '{result3}'"

    # Test with a non-integer string
    result4 = check_integer_string("ab4c")
    expected4 = "The string is not an integer."
    assert result4 == expected4, f"Test case 4 failed: Expected '{expected4}', but got '{result4}'"

    # Test with an empty string
    result5 = check_integer_string("")
    expected5 = "Input a valid text"
    assert result5 == expected5, f"Test case 5 failed: Expected '{expected5}', but got '{result5}'"
# Call the test function to execute the test cases
test_check_integer_string()