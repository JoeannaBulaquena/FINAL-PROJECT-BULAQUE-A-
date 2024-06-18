def measurement_converter():
    conversions = {
        '1': ("mm to cm", lambda x: x / 10),
        '2': ("cm to mm", lambda x: x * 10),
        '3': ("ft to m", lambda x: x * 0.3048),
        '4': ("m to ft", lambda x: x / 0.3048),
        '5': ("in to cm", lambda x: x * 2.54),
    }
    print("Choose a conversion:")
    for key, (description, _) in conversions.items():
        print(f"{key}: {description}")

    choice = input("Enter your choice: ")
    if choice in conversions:
        value = float(input("Enter the value to convert: "))
        description, conversion_func = conversions[choice]
        converted_value = conversion_func(value)
        print(f"{value} {description} is {converted_value}")
    else:
        print("Invalid choice")

measurement_converter()