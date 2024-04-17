print('Hello, world!')

user_name = input("Give your username:")
print(f"Hello {user_name.capitalize()}")

weight_in_kilogram = float(input("What's your weight in kilograms? "))
height_in_meters = float(input("What's your height in meters? "))
BMI = weight_in_kilogram / (height_in_meters*height_in_meters)
print(f"Your BMI is: {round(BMI,2)}.")
