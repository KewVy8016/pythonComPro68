try:
    value = int(input("Enter a number: "))
    result = 10/value
    print(f"Result is {result}")

except Exception as e:
    print(f"An error occurred: {e}") 
    
print("end the program")   