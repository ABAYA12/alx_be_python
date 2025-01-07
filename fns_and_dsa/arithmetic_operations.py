def perform_operation(num1=float, num2=float, operation=str):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "divide":
            return num1 / num2
        elif operation == "multiply":
            return num1 * num2
        else:
            print("Unknown operation. Please try again.")
    except ZeroDivisionError as e:
        print(e)
