'''
Activity 1: Errors
Incorporate the following code into a Python program to handle exceptions.
'''

def divide_numbers(a, b):
    '''
    Divides two numbers and handles potential errors.
    Returns the result or an error message.
    '''
    try:
        # Attempt to perform division
        result = int(a) / int(b)
        return result

    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numbers only"

    except (TypeError, ZeroDivisionError):
        # Handles division by zero and type errors
        return "Error: Cannot divide by zero or invalid input type"

    except:
        # Handles any other unexpected errors
        return "An unexpected error occurred"

print(divide_numbers(10, 2))    # Works correctly
print(divide_numbers(10, 0))    # Division by zero error
print(divide_numbers("ten", 2)) # Value error