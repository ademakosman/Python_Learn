#Data Types
# print(len(input("What is your name\n")))


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Turn to string to integer with int 
bmi = int(weight) /float(height)**2
print(bmi)
