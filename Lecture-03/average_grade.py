list_grade =[]

for i in range (3):
    grade_input = int(input(f"Enter the score for test {i+1}: "))
    list_grade.append(grade_input)

cal_average = sum(list_grade)/len(list_grade)
print(f"Your average score is {cal_average:.2f} ")

if cal_average > 95:
    print("Congratulation! your have a good average score")