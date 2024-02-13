# Request input from the user to input a string and assign it to the variable 'text'
text = input("Input a string: ")

# Remove leading and trailing whitespaces from the input string using the 'strip()' function
text = text.strip()

# Check if the length of the cleaned text is less than 1
if len(text) < 1:
    print("Input a valid text")  # If the text length is less than 1, display a message asking for valid input
else:
    # Check if all characters in the cleaned text are digits (0-9), indicating an integer
    if all(text[i] in "0123456789" for i in range(len(text))):
        print("The string is an integer.")  # If all characters are digits, display a message indicating an integer
    # Check if the text starts with a '+' or '-' and all subsequent characters are digits
    elif (text[0] in "+-") and all(text[i] in "0123456789" for i in range(1, len(text))):
        print("The string is an integer.")  # If the conditions for a signed integer are met, display an integer message
    else:
        print("The string is not an integer.")  # If none of the conditions are met, display a non-integer message