# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(float(weight/(height*height)))

if bmi < 18.5:
  print(f"your BMI = {bmi} you are under weight")
elif bmi < 25:
  print(f"your BMI = {bmi} you are normal weight")
elif bmi < 30:
  print(f"your BMI = {bmi} you are slightly weight")
elif bmi < 35:
  print(f"your BMI = {bmi} you are obese")    
else: 
  print(f"your BMI = {bmi} you are clinically obese")

