def perform_operation(num1, num2, operation):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "divide":
            if num2 != 0:
                return num1 / num2
            print('Number can not be divided by zero')

        elif operation == "multiply":
            return num1 * num2
        else:
            print("Unknown operation. Please try again.")
    except ValueError:
        print('please enter a number')
