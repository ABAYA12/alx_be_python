from robust_division_calculator import safe_divide

def main():
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()