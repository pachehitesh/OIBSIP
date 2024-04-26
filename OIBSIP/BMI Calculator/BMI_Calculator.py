def calculate_bmi(weight, height):   #Calculate the BMI (Body Mass Index) using weight in kilograms and height in meters. Formula: BMI = weight (kg) / (height (m) * height (m))
    bmi = weight / (height ** 2)
    return bmi
def result(bmi):   #Interpret the BMI value and return the corresponding category.
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"
def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = result(bmi)

    print(f"Your BMI is {bmi:.2f}, which is {category}.")


if __name__ == "__main__":
    main()