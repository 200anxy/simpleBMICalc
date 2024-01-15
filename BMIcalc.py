#BMI Calculator

import pyinputplus as pyip

weightinKG = pyip.inputInt("What is your weight in KG's?: ")
heightinM = pyip.inputInt("What is your height in CM's?: ")

bmi = weightinKG/(heightinM*heightinM)
print(f'Your BMI is {bmi}')

if bmi >= 30:
    print("Your BMI reading reads OBESE")
elif 25<= bmi<=29.9:
    print("Your BMI reading reads OVERWEIGHT")
elif 18.5<= bmi <=24.9:
    print("Your BMI reading reads NORMAL WEIGHT! GOOD JOB")
elif bmi<=18.5:
    print("Your BMI reading reads UNDERWEIGHT")