def safe_divide(numerator, denominator):
    """
    Safely performs division, handling errors like division by zero and non-numeric inputs.

    Args:
        numerator: The numerator for the division (expected to be convertible to float).
        denominator: The denominator for the division (expected to be convertible to float).

    Returns:
        str: The result of the division or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."
