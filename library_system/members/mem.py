class ValueTooHighError(Exception)
   def __init__(self, value):
        self.value = value

    def __str__(self):
        return f" Sorry the value you entered is too high. '{self.value}' should be less than 100"


def housing(value):
    housing_list = []
    try:
        house_number = float(input("Enter house number (1 -100): "))s
        if house_number > 100:
            raise ValueTooHighError(house_number)
        elif house_number in housing_list:
            print(f"Sorry, house number {house_number} is already available. Please enter the correct house number.")
        return housing_list.append(house_number)
    except ValueError:
        print(f"Sorry, you entered a wrong value {house_number}")
    else:
        print(f"House number: {house_number} added successfully.")
    finally:
        print('Byee')
    

housing()