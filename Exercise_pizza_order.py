# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Exercise
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1 👇
size_price = 0
total_price = 0
if size == "S":
  size_price += 15
  if add_pepperoni == "Y":
    size_price = size_price + 2
    if extra_cheese == "Y":
      size_price = size_price + 1
elif size == "M":
  size_price += 20
  if add_pepperoni == "Y":
    size_price = size_price + 3
    if extra_cheese == "Y":
      size_price = size_price + 1
elif size == "L":
  size_price = 25
  if add_pepperoni == "Y":
    size_price = size_price + 3
    if extra_cheese == "Y":
      size_price = size_price + 1
print(f"Your pizza size {size} and ${size_price} total bill")




