
weight_in_kilogram = float(input("What's your weight in kilograms? "))
height_in_meters = float(input("What's your height in meters? "))
if weight_in_kilogram == 0 or height_in_meters == 0:
    print("Can't divide by zero!")
    
else:
    BMI = weight_in_kilogram / height_in_meters**2
    print(f"Your BMI is: {round(BMI,2)}")
    if BMI < 16.0:
        print("Underweight (Severe thinness)")
    elif 16.0 <= BMI <=16.9:
        print("Underweight (Moderate thinness)")
    elif  17.0 <= BMI <=18.4:
        print("Underweight (Mild thinness)")
    elif  18.5 <= BMI <=24.9:
        print("Normal range")
    elif  25.0 <= BMI <=29.9:
        print("Overweight (Pre-obese)")
    elif  30.0 <= BMI <=34.9:
        print("Obese (Class I)")
    elif  35.0 <= BMI <=39.9:
        print("Obese (Class II)")
    elif BMI >= 40.0: 
        print("Obese (Class II)")

#Underweight (Severe thinness)	< 16.0	< 0.64
#Underweight (Moderate thinness)	16.0 – 16.9
#Underweight (Mild thinness)	17.0 – 18.4	
#Normal range	18.5 – 24.9	
#Overweight (Pre-obese)	25.0 – 29.9	
#Obese (Class I)	30.0 – 34.9	
#Obese (Class II)	35.0 – 39.9	
#Obese (Class III)	≥ 40.0
