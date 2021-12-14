sum_numbers = 0
# for even_number in range(0,101,2): work every 2 steps
for even_number in range(0,101):
  if (even_number % 2) == 0:
    sum_numbers += even_number
print("Even numbers total is =",sum_numbers)