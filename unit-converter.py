def is_valid_input(input_str):
    try:
        # Try to convert the input to a float
        float(input_str)
        return True
    except ValueError:
        return False

def convert_unit(value):
    # For this example, let's convert kilometers to miles
    # You can modify this function to include more conversions
    km = float(value)
    miles = km * 0.621371
    return f"{km} kilometers is equal to {miles:.2f} miles"

def unit_converter():
    while True:
        print("Enter a distance in kilometers (or 'q' to quit):")
        user_input = input()
        
        if user_input.lower() == 'q':
            print("Exiting the converter. Goodbye!")
            break
        
        if is_valid_input(user_input):
            result = convert_unit(user_input)
            print("Result:", result)
        else:
            print("Invalid input. Please enter a valid number.")

# Run the unit converter
print("Unit Converter: Kilometers to Miles")
unit_converter()