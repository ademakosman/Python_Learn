# True Love Program 
# lower_name = "Adem".lower()
# lower_name.count("a")

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
count_t = lower_name1.count("t") + lower_name2.count("t")
count_r = lower_name1.count("r") + lower_name2.count("r")
count_u = lower_name1.count("u") + lower_name2.count("u")
count_e = lower_name1.count("e") + lower_name2.count("e")
count_l = lower_name1.count("l") + lower_name2.count("l")
count_o = lower_name1.count("o") + lower_name2.count("o")
count_v = lower_name1.count("v") + lower_name2.count("v")
count_e = lower_name1.count("e") + lower_name2.count("e")
count_first = count_t + count_r + count_u + count_e
count_second = count_l + count_o + count_v + count_e
score = int(str(count_first) + str(count_second))

if (score <10) or (score>90):
  print(f"love Score {score} , You go together like coke and mentos")
elif (score <50) and (score>40):
    print(f"love Score {score} , You go all right together")
else:
    print(f"love Score {score} ")

