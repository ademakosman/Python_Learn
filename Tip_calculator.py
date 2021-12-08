#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Wellcome to the tip calculator\n ")
total_bill = input(print("what was the total bill? "))
tip_percent = input(print("what percentage tip would you like to give? 10, 12 or 15?"))
split = input(print("how many people to slipt the bill? "))
each_pay = (float(total_bill)/int(split))*(1+(float(tip_percent)/100))
each_pay = round(each_pay,2)
print(f"each person should pay {each_pay}")