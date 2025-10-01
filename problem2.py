"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    # TODO: Implement this function
    return (celsius * 9 / 5) + 32 


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    # TODO: Implement this function
    return (fahrenheit - 32) * 5 / 9


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    value = input("Enter the temperature value: ")
    # - Get unit (C or F) from user
    unit = input("Is it in Celcious (C) or Fahrenheit (F)?") 
    # - Validate input
    if unit == "C": 
        result = celcius_to_fahrenheit(value)
        print(round(value, 2), "C° =", round(result, 2), "F°")
    elif unit == "F":
        result = fahrenheit_to_celcius(value)
        print(round(value, 2), "F° =", round(result, 2), "C°")
    else: 
        print("Invalid unit. Please enter C or F.")
    # - Perform conversion
    # - Display result rounded to 2 decimal places

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()
