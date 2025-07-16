print("Select operation -\n1. Add\n2.Subtract\n3.Multiply\n4.Divide")
operation = int(input("Select operation form  1,2,3,4 : "))
input_1 = int(input("Enter first number: "))
input_2 = int(input("Enter second number: "))

if operation == 1:
    print(f"Summary value:{input_1} + {input_2} = {input_1+input_2}")
elif operation == 2:
    print(f"Summary value:{input_1} - {input_2} = {input_1-nput_2} ")
elif operation == 3:
    print(f"Summary value:{input_1} * {input_2} = {input_1*input_2}")
elif operation == 4:
    print(f"Summary value:{input_1} / {input_2} = {input_1/input_2}")