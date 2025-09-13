try:
    value = int(input("Enter a number: "))
    result = 10/value
except ZeroDivisionError as e:
    print("Can not divide by zero")
else:
    print(f"The result is result    {result}") 
    
    
print("End of program")