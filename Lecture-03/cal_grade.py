score = int(input("Enter your score: "))

if score < 1:
    print ("Invalid score")
elif score < 50:
    print("Your grade : D or F")
elif score <80:
    print("your grade : C")
elif score <90:
    print("your grade : B")
else :
    print("your grade : A")