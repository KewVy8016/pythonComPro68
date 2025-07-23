score = int(input("Enter your score: "))

while score < 0 or score > 100:
    print("Invalid score pls enter score 0 - 100")
    score = int(input("Enter your score: "))
print(f"your score is: {score} ")