student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
#Write your code below this row 👇
big_score = 0
for score in student_scores:
  if score > big_score:
    big_score = score

print("big score is ",big_score)

